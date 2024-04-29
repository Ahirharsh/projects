import streamlit as st
from model import SentimentRecommenderModel

# Create an instance of the SentimentRecommenderModel
sentiment_model = SentimentRecommenderModel()

# Define the Streamlit app
def main():
    st.title('Sentiment Based Product Recommendation')

    # Display a form to input username
    username = st.text_input('Enter UserName to search')

    if st.button('Submit'):
        if username:
            # Retrieve recommendations based on username
            items = sentiment_model.getSentimentRecommendations(username.lower())
            if items is not None:
                st.write('List of Top 5 Recommended Products:')
                st.table(items.head())
            else:
                st.warning("User Name doesn't exist. No product recommendations at this point of time!")

    # Display a form to input review text
    review_text = st.text_area('Enter your Review here')

    if st.button('Predict Sentiment'):
        if review_text:
            # Predict sentiment based on review text
            pred_sentiment = sentiment_model.classify_sentiment(review_text)
            if pred_sentiment == 1:
                 st.success('Entered Review Text is predicted to be Positive')
            elif pred_sentiment == 0:
                 st.error('Entered Review Text is predicted to be Neutral')
            else:
                 print("Entered Review Text is predicted to be Negative")


if __name__ == '__main__':
    main()
