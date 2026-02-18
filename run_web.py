"""
Quick start script for Brand Agent Web Application
"""
import subprocess
import sys
import os

def main():
    print("=" * 60)
    print("🚀 Brand Agent System - Web Application")
    print("=" * 60)
    print()
    
    # Check if in correct directory
    if not os.path.exists('web_app.py'):
        print("❌ Error: Please run this script from the brand_agent directory")
        sys.exit(1)
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("⚠️  Warning: .env file not found!")
        print("   Creating from .env.example...")
        if os.path.exists('.env.example'):
            with open('.env.example', 'r') as src:
                content = src.read()
            with open('.env', 'w') as dst:
                dst.write(content)
            print("   ✅ Created .env file. Please add your API keys.")
        else:
            print("   ❌ .env.example not found. Please create .env manually.")
    
    print()
    print("Starting Flask web server...")
    print()
    print("📱 Once started, open your browser to:")
    print("   http://localhost:5000")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    print()
    
    try:
        # Run the Flask app
        subprocess.run([sys.executable, 'web_app.py'], check=True)
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
