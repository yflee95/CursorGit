import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('palindrome.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def is_palindrome(word):
    """
    Check if a word or phrase is a palindrome with detailed logging.
    
    Args:
        word: Input string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    logger.info(f"Starting palindrome check for input: '{word}' (type: {type(word).__name__})")
    
    try:
        # Log input validation
        if word is None:
            logger.error("Input is None - cannot process")
            raise TypeError("Input cannot be None")
        
        if not isinstance(word, str):
            logger.warning(f"Input is not a string (type: {type(word).__name__}), attempting conversion")
            word = str(word)
            logger.info(f"Converted input to string: '{word}'")
        
        # Log original input details
        original_length = len(word)
        logger.info(f"Original input length: {original_length} characters")
        
        # Track character cleaning process
        logger.info("Starting character cleaning process...")
        
        # Log each character being processed
        cleaned_chars = []
        removed_chars = []
        
        for i, char in enumerate(word):
            if char.isalnum():
                cleaned_chars.append(char.lower())
                logger.debug(f"Character {i}: '{char}' -> '{char.lower()}' (kept)")
            else:
                removed_chars.append(char)
                logger.debug(f"Character {i}: '{char}' (removed - not alphanumeric)")
        
        # Log cleaning summary
        logger.info(f"Cleaning complete: {len(cleaned_chars)} characters kept, {len(removed_chars)} characters removed")
        if removed_chars:
            logger.info(f"Removed characters: {removed_chars}")
        
        # Join cleaned characters
        cleaned = ''.join(cleaned_chars)
        logger.info(f"Cleaned string: '{cleaned}' (length: {len(cleaned)})")
        
        # Check if cleaned string is empty
        if not cleaned:
            logger.info("Cleaned string is empty - considering as palindrome")
            return True
        
        # Create reversed string for comparison
        reversed_cleaned = cleaned[::-1]
        logger.info(f"Reversed string: '{reversed_cleaned}'")
        
        # Perform comparison
        is_palindrome_result = cleaned == reversed_cleaned
        logger.info(f"Comparison result: '{cleaned}' == '{reversed_cleaned}' -> {is_palindrome_result}")
        
        # Log final result with details
        if is_palindrome_result:
            logger.info(f"✅ '{word}' IS a palindrome")
        else:
            logger.info(f"❌ '{word}' is NOT a palindrome")
        
        return is_palindrome_result
        
    except Exception as e:
        logger.error(f"Error processing input '{word}': {str(e)}")
        raise
