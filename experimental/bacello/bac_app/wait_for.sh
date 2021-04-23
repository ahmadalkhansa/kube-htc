#!/bin/bash
#basescript to fix the order of container
#based on the name of the container
#will wait for seconds for the process to end, and if timeout not specified, will wait until the status of the container is exited

cmdname=$(basename $0)

echoerr() { if [[ $QUIET -ne 1 ]]; then echo "$@" 1>&2; fi }

usage()
{
        cat << USAGE >&2
Usage:
        $cmdname 
                -n                  Wait until the named container exit, and return its exit code
                -t                  Timeout, default is not to wait at all (just check and exit), zero for no timeout
                -s|--strict         Only execute subcommand if the test succeeds
                -h|--help           Show this message
                -- COMMAND ARGS     Execute command with args after the test finishes
USAGE
        exit 1
}

wait_for()
{
        if [[ $TIMEOUT -gt 0 ]]; then
                CHECK=-1
                echoerr "$cmdname: waiting $TIMEOUT seconds for container $NAME"
        else
                CHECK=0
                echo $TIMEOUT
                echo $CHECK 
                echoerr "$cmdname: waiting for $NAME without a timeout"
        fi

        start_ts=$(date +%s)
        while :
        do
                #echo  $(docker ps -a )
                STATUS=$( docker container inspect -f '{{.State.Status}}' "$NAME" )
                #STATUS=$(docker inspect $(docker-compose ps -q "$NAME" 2>/dev/null) 2>/dev/null | jq -r .[0].State.Status)
                echo "Status :""$STATUS"
                #check the status of the container using the docker inspection function and the name of the container: 
                #if the container is exited, so it has finish its operations:

                if [[ "$STATUS" == "exited" ]]; then

                        RESULT=$(docker container inspect -f '{{.State.ExitCode}}' "$NAME")
                        #saving the exit code of the container
                        echo $RESULT
                        end_ts=$(date +%s)
                        if [[ $CHECK -eq -1  ]]; then                   #timeout greater than 0 (always greater)
                                echoerr "$cmdname: container $NAME exited after $((end_ts - start_ts)) seconds with exit code: $RESULT"
                        else
                                echoerr "$cmdname: container $NAME exit code: $RESULT"
                        fi
                        return $RESULT

                #if status is not exited, so container still no finished
                else
                        echo "Not exited so:" "$STATUS"
                        if [[ $CHECK -eq 0 ]]; then             #timeout greater than -1 
                                if [[ -z "$STATUS" ]]; then                      #if the status does not exist
                                        echoerr "$cmdname: container $NAME not running"
                                else
                                        echoerr "$cmdname: container $NAME status: $STATUS"
                                fi
                                #return 1
                        fi


                        if [[ $CHECK -eq -1 ]] && [[ $((end_ts - start_ts)) -gt $TIMEOUT ]]; then
                                 echoerr "$cmdname: timeout occurred after waiting $TIMEOUT seconds for container $NAME"
                        #timeout greater than 0 and time used by the container is greater than the actual timeout set (so taking more time than set): problems!
                                if [[ -z "$STATUS"  ]]; then                      #if the status does not exist
                                        echoerr "$cmdname: container $NAME not running"
                                else
                                        echoerr "$cmdname: container $NAME status: $STATUS"
                                fi
                        fi
                fi
                sleep 5
        done
}

STRICT=0
TIMEOUT=-1
NAME=
COMMAND=

#PROCESSING INPUTS:
while [[ $# -gt 0 ]]
do
        case "$1" in
                -n)
                        NAME="$2"
                        shift 2
                        ;;
                -s|--strict)
                        STRICT=1
                        shift 1
                        ;;
                -t)
                        TIMEOUT="$2"
                        shift 2
                        ;;
                -h|--help)
                        usage
                        ;;
                --)
                        shift
                        COMMAND="$@"
                        break
                        ;;
                *)
                        echoerr "Unknown argument: $1"
                        usage
                        ;;
        esac
done


#CALLING HERE THE REAL FUNCTION:
if [[ "$NAME" == "" ]]; then
        echoerr "Error: you need to provide a container name"
        usage
fi

wait_for
#echo $RESULT
RESULT=$?
echo $RESULTS
if [[ $COMMAND != "" ]]; then
        if [[ $RESULT -ne 0 && $STRICT -eq 1 ]]; then
                echoerr "$cmdname: strict mode, refusing to execute subprocess"
                exit $RESULT
        fi
        exec $COMMAND
else
        exit $RESULT
fi


