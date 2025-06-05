# import nltk

# # Download data to a custom folder named 'nltk_data' in your current directory
# nltk.download('punkt', download_dir='./nltk_data')
# nltk.download('stopwords', download_dir='./nltk_data')
import nltk
import os

# Create nltk_data directory in current path
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
os.makedirs(nltk_data_dir, exist_ok=True)

# Set NLTK path manually
nltk.data.path.append(nltk_data_dir)

# Download only stopwords
nltk.download('stopwords', download_dir=nltk_data_dir)

print(f"Downloaded 'stopwords' to: {nltk_data_dir}")
