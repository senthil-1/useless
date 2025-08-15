# 🍽️ FridgeMood.AI

**Discover the secret emotional lives of your fridge contents!**

FridgeMood.AI uses AI to detect items in your fridge and assigns them hilarious, random personalities. Each upload generates completely unique moods for your food items.

## ✨ Features

- 🤖 **AI Object Detection** - Detects items in your fridge photos
- 🎭 **Random Mood Generation** - Each item gets a unique personality every time
- 🚫 **No Duplicates** - Each item appears only once in analysis
- 📱 **Mobile Friendly** - Works perfectly on all devices
- ⚡ **No Page Reloads** - Smooth upload experience
- 🎨 **Beautiful UI** - Animated fridge interface with ice cubes

## 🎯 Example Output

```
bottle – "Plotting a rebellion against expiration dates"
orange – "Writing poetry about the meaning of cold"
milk – "Becoming a therapist for traumatized leftovers"

Final Mood: Your fridge is having a midlife crisis
```

## 🚀 Live Demo

**[Try FridgeMood.AI Live!](https://your-app-url.vercel.app)** *(Deploy to get your URL)*

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python Flask
- **AI**: YOLO object detection
- **Deployment**: Vercel
- **Styling**: Custom CSS with animations

## 📁 Project Structure

```
fridgemood-ai/
├── index12.html          # Main frontend application
├── api/
│   └── app.py            # Flask backend API
├── app_final_random.py   # Local development server
├── vercel.json           # Vercel deployment config
├── requirements.txt      # Python dependencies
├── deploy.bat            # Deployment script
└── README.md             # This file
```

## 🏃‍♂️ Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the local server**
   ```bash
   python app_final_random.py
   ```

4. **Open your browser**
   ```
   http://localhost:5000
   ```

### Deploy to Vercel

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Deploy**
   ```bash
   vercel
   ```

3. **Or use the deployment script**
   ```bash
   deploy.bat
   ```

## 🎮 How to Use

1. **Open the app** in your browser
2. **Click the fridge handle** to open it
3. **Upload a photo** of your fridge contents
4. **Watch the magic happen** as AI analyzes your food
5. **Enjoy the hilarious moods** assigned to each item!

## 🎨 Features Showcase

### Random Mood Examples
Your items might get personalities like:
- *"Having a philosophical debate with the light bulb"*
- *"Starting a podcast about cold storage"*
- *"Practicing interpretive dance in the dark"*
- *"Writing angry reviews about your eating habits"*

### No Duplicates
Even if YOLO detects "2 bottles", you'll only see one bottle entry with a unique mood.

### Mobile Responsive
Works perfectly on phones, tablets, and desktops with touch-friendly controls.

## 🔧 Development

### Key Files

- **`index12.html`** - Main frontend with fridge animation
- **`app_final_random.py`** - Local development server with YOLO
- **`api/app.py`** - Vercel-optimized backend with fallback detection

### Adding New Moods

Edit the `all_moods` array in the mood generation function to add new personalities!

## 🐛 Known Issues

- YOLO model may occasionally misidentify items (books as chocolate bars)
- Large images may take longer to process
- Some mobile browsers may have upload limitations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **YOLO** for object detection
- **Flask** for the backend framework
- **Vercel** for hosting
- **OpenAI** for inspiration on AI applications

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/your-repo-name/issues) page
2. Create a new issue if needed
3. Review the deployment guide in `DEPLOYMENT_GUIDE.md`

---

**Made with ❤️ and a lot of ☕**

*Give your fridge the personality analysis it deserves!* 🍽️✨
