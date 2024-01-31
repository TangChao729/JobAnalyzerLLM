import PySimpleGUI as sg

def get_user_input():
    # Define the layout of the window
    layout = [
        [sg.Text('Choose your experience level:'), sg.Combo(['Junior', 'Mid-Senior', 'Executive', 'Casual'], key='experience')],
        [sg.Text('Choose your preferred country:'), sg.Combo(['United States', 'Singapore', 'Australia', 'Canada'], key='country')],
        [sg.Text('Enter the job title:'), sg.InputText(key='job_title')],
        [sg.Submit(), sg.Cancel()]
    ]

    # Create the window
    window = sg.Window('Job Search Query', layout)

    # Event loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):  # If user closes window or clicks cancel
            break
        if event == 'Submit':
            window.close()
            return values

    window.close()

# Example usage
user_query = get_user_input()
print("\nUser Query Info:")
print(user_query)
