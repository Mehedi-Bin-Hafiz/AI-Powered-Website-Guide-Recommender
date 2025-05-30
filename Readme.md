# AI-Powered Website Guide Recommender

<p align="center">
  <img src="./docs/architecture.png" alt="System Architecture" width="600">
  <br>
  <em>System Architecture Overview</em>
</p>

## 🔍 Overview

An intelligent chatbot that scrapes websites, creates semantic embeddings of content, and provides users with the most relevant links based on their natural language queries. This tool eliminates the need to manually browse through websites by understanding user intent and returning precise, contextually relevant links.

## ✨ Key Features

- **🕷️ Smart Web Scraping**: Automatically extracts links and associated text from any website
- **🧠 Semantic Understanding**: Uses sentence transformers to understand query meaning beyond keyword matching
- **⚡ Fast Vector Search**: ChromaDB-powered similarity search for instant results
- **💾 Intelligent Caching**: Daily caching system to avoid redundant scraping
- **🤖 Interactive Chatbot**: Conversational interface for natural query interaction
- **🎯 Precise Recommendations**: Returns the most relevant link based on semantic similarity

## 🏗️ Architecture

The system follows a multi-stage pipeline:

1. **Data Ingestion**: Web scraper extracts links and text content
2. **Text Processing**: Content is cleaned and normalized
3. **Embedding Generation**: Sentence transformers create vector representations
4. **Vector Storage**: ChromaDB stores embeddings for fast retrieval
5. **Query Processing**: User queries are embedded and matched against stored vectors
6. **Result Ranking**: Most semantically similar content is returned

## 🚀 Quick Start

### Prerequisites

```bash
pip install chromadb sentence-transformers requests beautifulsoup4 tqdm
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Mehedi-Bin-Hafiz/AI-Powered-Website-Guide-Recommender.git
cd AI-Powered-Website-Guide-Recommender
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the chatbot**
```bash
python chatbot.py
```

### Usage Example

```bash
# Start the application
python chatbot.py

# Enter website URL when prompted
Give me website link: https://example-university.edu

# Wait for data processing
Learning the data...
Learning complete! Ask me anything or type "exit" to stop:

# Ask natural language questions
Enter your query: admission requirements
The best matching link for your query is: https://example-university.edu/admissions/requirements

Enter your query: computer science courses
The best matching link for your query is: https://example-university.edu/academics/computer-science

Enter your query: exit
Exiting the chatbot...
```

## 📁 Project Structure

```
AI-Powered-Website-Guide-Recommender/
├── chatbot.py                 # Main chatbot application
├── WebChatbot/
│   └── daily_scrapping.py    # Web scraping module
├── docs/
│   └── architecture.png      # System architecture diagram
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
└── LICENSE                  # MIT License
```

## 🔧 Technical Details

### Core Components

#### 1. Web Scraper (`daily_scrapping.py`)
- **BeautifulSoup4** for HTML parsing
- **Requests** for HTTP operations
- **Smart caching** to avoid daily re-scraping
- **Text cleaning** and normalization
- **URL resolution** for relative links

#### 2. Vector Database (`chatbot.py`)
- **ChromaDB** for embedding storage and retrieval
- **Sentence Transformers** (`paraphrase-MiniLM-L6-v2`) for embeddings
- **Semantic search** using cosine similarity
- **Real-time query processing**

### Key Functions

```python
# Scraping function with caching
def daily_scraper(url)
    # Returns cached data if scraped today, else scrapes fresh

# Query processing function  
def find_best_link(query)
    # Embeds query and finds most similar content
```

## 🛠️ Configuration

### Embedding Model
The system uses `paraphrase-MiniLM-L6-v2` by default. You can modify this in `chatbot.py`:

```python
embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="your-preferred-model"
)
```

### Search Results
Currently returns top 1 result. Modify `n_results` parameter for multiple results:

```python
results = collection.query(query_embeddings=query_embedding, n_results=5)
```

## 📊 Performance Considerations

- **Caching**: Daily cache reduces scraping overhead
- **Embedding Model**: Lightweight model balances speed and accuracy
- **Vector Database**: ChromaDB provides fast similarity search
- **Memory Usage**: Scales with website size and content volume

## 🔮 Future Enhancements

- [ ] **Multi-language Support**: Handle queries in different languages
- [ ] **Advanced Models**: Integration with larger transformer models
- [ ] **Web Interface**: Flask/Django web application
- [ ] **Result Ranking**: Multiple relevance factors beyond similarity
- [ ] **Content Filtering**: Ignore navigation/footer links
- [ ] **Batch Processing**: Handle multiple websites simultaneously
- [ ] **API Endpoints**: RESTful API for integration
- [ ] **Analytics Dashboard**: Query patterns and performance metrics

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/AI-Powered-Website-Guide-Recommender.git
cd AI-Powered-Website-Guide-Recommender

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mehedi Bin Hafiz**
- GitHub: [@Mehedi-Bin-Hafiz](https://github.com/Mehedi-Bin-Hafiz)

## 🙏 Acknowledgments

- **Sentence Transformers** team for the embedding models
- **ChromaDB** for the vector database solution
- **BeautifulSoup** for web scraping capabilities

## 📈 Use Cases

- **Educational Websites**: Quickly find course information, requirements, faculty details
- **E-commerce Sites**: Locate specific products or categories
- **Documentation Sites**: Find relevant API endpoints or guides
- **News Websites**: Discover articles on specific topics
- **Corporate Websites**: Navigate to specific departments or services

## 🐛 Issues and Support

If you encounter any issues or have questions:

1. Check existing [Issues](https://github.com/Mehedi-Bin-Hafiz/AI-Powered-Website-Guide-Recommender/issues)
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

---

<p align="center">
  Made with ❤️ by Mehedi Bin Hafiz
</p>