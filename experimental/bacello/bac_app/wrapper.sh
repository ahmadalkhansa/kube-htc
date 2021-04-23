#Starting second process, only if the first has been coming out good.
./recognition.sh -D
#echo "Recognition.."
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to start the application Bacello: $status"
        exit $status
fi              
