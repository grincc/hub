# The script will scan ports with specific IPs, then send the result to specific email in every x hours by crontab 
#!/bin/sh

output="/root/multiple_port_scan_result.log"
recipient="sender@email.com"
sender_name="Sender name"
sender_email="receiver@email.com"
# Get current date and time in UTC
current_datetime=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

# Create a custom subject with the current date and time
subject="Grin nodes results $current_datetime"
# Clear the output file or create a new one
> "$output"
#server-list.txt contains IP addresss in each line and port-list.txt contains ports, grin node port is 3414. Those files are in same directory.
for server in $(cat server-list.txt);
do
        for port in $(cat port-list.txt);
        do
                #echo $server
                nc -zvw3 "$server" "$port" 2>&1 | tee -a "$output"
                echo "" >> "$output"
done
done
# Read the content of the output file into the email body
email_body=$(cat "$output")

# Send the email using the mail command with sender's name, email, subject, and body
# Sending email by postfix, I use ISPConfig to configure Email routing/Relay pointing to use another trusted smtp to send email.
(
echo "Subject: $subject"
echo "To: $recipient"
echo "From: $sender_name <$sender_email>"
echo
echo "$email_body"
) | /usr/sbin/sendmail -t -oi

