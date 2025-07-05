log_format="clean_log.log"
log_path="$HOME"
log_file="$log_path/$log_format"
save_days = 10

log_path_clean="/tmp"
find ${log_path_clean} -type f -name
 "${log_format}" -maxdepth 1 -ctime ${save_days}
  -execdir rm -f '{}' \;
  rc =$? 
  if [ $rc -ne 0 ]; then
  logger -s "log clean successful"
  cat >> ${log_file} << EOF
  "date": ${date +%Y-%m-%dT%H:%M:%S%z},
  "operation": "find ${save_days} days have been removed from type f -name "*.log" -maxdepth 1 -ctime 
  ${save_days} -execdir rm -f '{}' \;",
    msg "clean ok",

eof
else
    echo "Error: Failed to clean old log files."
    logger -s "log clean failed"
    exit 1
  fi

  if test -s ${log_file}; then
    find ${log_file} -type f -name"
    *.log
echo "Old log files older than ${save_days} days have been removed from ${log_path