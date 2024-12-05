while true; do
    curl -s "https://hand-image-recognition-group07.onrender.com" > /dev/null
    echo "Ping sent at $(date)"
    sleep 840     # Ping the server every 14 minutes.
done