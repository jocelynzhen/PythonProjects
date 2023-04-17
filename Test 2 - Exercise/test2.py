# Define the list of valid channels
VALID_CHANNELS = ['TV1', 'TV2', 'TV3', 'NTV7', 'TV8']

# Define a function to check if a given channel is valid
def is_valid_channel(channel):
    return channel.upper() in VALID_CHANNELS

# Define a function to read and save the channel to a file
def TVChannel():
    while True:
        channel = input('Enter a TV channel: ')
        if is_valid_channel(channel):
            with open('channel.txt', 'w') as file:
                file.write(channel.upper())
            print('Channel saved to file.')
            break
        else:
            print('Wrong Channel')

# Define a function to read the channel from the file and display it
def display_channel():
    with open('channel.txt', 'r') as file:
        channel = file.read()
        if channel:
            print('The current TV channel is:', channel)
        else:
            print('No TV channel saved.')

# Call the TVChannel function to get a channel from the user and save it to a file
TVChannel()

# Call the display_channel function to read and display the channel from the file
display_channel()
