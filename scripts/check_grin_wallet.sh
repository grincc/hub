#Script to monitor mass grin wallets status and send email periodically with crontab
#!/bin/bash

# Set the recipient's email address
recipient_email="support@grinbux.com"

# Set the sender's name and email address
sender_name="Grin Archive Node Chicago"
sender_email="support@grinbux.com"

# Get current date and time in UTC
current_datetime=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

# Define the subject of the email
email_subject="Grin Wallets Check - $current_datetime"

# Read the list of Grin wallet addresses from an external file grin_wallet_addresses.txt in same directory
wallet_addresses_file="grin_wallet_addresses.txt"
wallet_addresses=($(cat "$wallet_addresses_file"))

# Initialize a variable to store the email content
email_content=""

# Initialize a variable to store the terminal output
terminal_output=""

# Loop through each wallet address and check its status, jq package should be installed in linux
for grin_address in "${wallet_addresses[@]}"; do
    response=$(curl -s "https://grinnode.live:8080/walletcheck/$grin_address")
    is_wallet_valid=$(echo "$response" | jq -r '.isWalletValid')

    if [ "$is_wallet_valid" == "true" ]; then
        result="Grin address $grin_address is online."
    elif [ "$is_wallet_valid" == "false" ]; then
        result="Grin address $grin_address is not online."
    else
        result="Unable to determine status for Grin address $grin_address."
    fi

    email_content+="\n$result"
    terminal_output+="\n$result"
done

# Display the results in the terminal
echo -e "Grin Wallets Check Results:$terminal_output"

# Send the email with the results
echo -e "$email_content" | mail -s "$email_subject" -a "From: $sender_name <$sender_email>" "$recipient_email"
