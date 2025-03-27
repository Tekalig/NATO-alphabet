# NATO Alphabet

This project converts a user-provided word into its corresponding NATO phonetic alphabet representation.
## Requirements

To run this project, you need the following:

- Python 3.6 or higher
- A `requirements.txt` file with the necessary dependencies. Install them using:
    ```
    pip install -r requirements.txt
    ```
## How to Use

1. Ensure you have a CSV file named `nato_phonetic_alphabet.csv` in the `data` directory. The file should contain two columns: `letter` and `code`, where `letter` represents the alphabet and `code` represents the phonetic word.

2. Run the `main.py` script.

3. Enter a word when prompted. The script will output the NATO phonetic alphabet representation of the word.

4. To exit the program, type `EXIT`.

## Example

```
Enter your word: hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']

Enter your word: exit
['Echo', 'X-ray', 'India', 'Tango']

Enter your word: EXIT
