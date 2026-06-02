"""
Auto-Local Palestine - Main Flask Application
Smart Car Parts & Services Finder with AI Chatbot
"""
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from config import get_config
from utils.gemini_ai import get_chatbot

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, 
            template_folder='../frontend',
            static_folder='../frontend')

# Configure Flask
config = get_config()
app.config.from_object(config)

# Enable CORS
CORS(app)

# Initialize chatbot
try:
    chatbot = get_chatbot()
    chatbot_ready = True
except Exception as e:
    print(f"⚠️ Chatbot initialization error: {e}")
    chatbot_ready = False

# ==================== ROUTES ====================

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "app": "Auto-Local Palestine",
        "version": "1.0.0",
        "chatbot": "ready" if chatbot_ready else "error"
    })

# ==================== CHATBOT ROUTES ====================

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat endpoint - Send message to chatbot"""
    try:
        if not chatbot_ready:
            return jsonify({
                "success": False,
                "error": "البوت غير متاح حالياً"
            }), 503
        
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                "success": False,
                "error": "الرسالة فارغة"
            }), 400
        
        # Get chatbot response
        response = chatbot.chat(user_message)
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/chat/recommendations', methods=['POST'])
def get_recommendations():
    """Get AI recommendations for car problem"""
    try:
        if not chatbot_ready:
            return jsonify({
                "success": False,
                "error": "البوت غير متاح حالياً"
            }), 503
        
        data = request.get_json()
        problem = data.get('problem', '').strip()
        
        if not problem:
            return jsonify({
                "success": False,
                "error": "الرجاء وصف المشكلة"
            }), 400
        
        response = chatbot.get_recommendations(problem)
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/chat/maintenance-tips', methods=['GET'])
def get_maintenance():
    """Get maintenance tips from AI"""
    try:
        if not chatbot_ready:
            return jsonify({
                "success": False,
                "error": "البوت غير متاح حالياً"
            }), 503
        
        car_model = request.args.get('model', None)
        response = chatbot.get_maintenance_tips(car_model)
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/chat/clear', methods=['POST'])
def clear_chat():
    """Clear chat history"""
    try:
        if chatbot_ready:
            chatbot.clear_history()
        return jsonify({
            "success": True,
            "message": "تم مسح سجل المحادثة"
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# ==================== PARTS ROUTES ====================

@app.route('/api/parts', methods=['GET'])
def get_parts():
    """Get car parts"""
    try:
        # TODO: Fetch from database
        return jsonify({
            "success": True,
            "parts": []
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/parts/<int:part_id>', methods=['GET'])
def get_part(part_id):
    """Get specific part details"""
    try:
        # TODO: Fetch from database
        return jsonify({
            "success": True,
            "part": {}
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# ==================== SERVICES ROUTES ====================

@app.route('/api/services', methods=['GET'])
def get_services():
    """Get available services"""
    try:
        services = [
            {"id": 1, "name": "ميكانيك", "icon": "🔧"},
            {"id": 2, "name": "كهرباء السيارات", "icon": "⚡"},
            {"id": 3, "name": "بنشر وإطارات", "icon": "🔴"},
            {"id": 4, "name": "غسيل وتلميع", "icon": "💧"},
            {"id": 5, "name": "قطع غيار", "icon": "📦"},
            {"id": 6, "name": "هيكل وديهان", "icon": "🚗"},
            {"id": 7, "name": "فحص فني", "icon": "🔍"},
            {"id": 8, "name": "إنقاذ وسحب", "icon": "🚛"},
        ]
        return jsonify({
            "success": True,
            "services": services
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# ==================== BOOKINGS ROUTES ====================

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    """Get user bookings"""
    try:
        # TODO: Fetch from database
        return jsonify({
            "success": True,
            "bookings": []
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """Create new booking"""
    try:
        data = request.get_json()
        # TODO: Save to database
        return jsonify({
            "success": True,
            "message": "تم حجز الموعد بنجاح",
            "booking": {}
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# ==================== REVIEWS ROUTES ====================

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    """Get reviews and ratings"""
    try:
        # TODO: Fetch from database
        return jsonify({
            "success": True,
            "reviews": []
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/reviews', methods=['POST'])
def create_review():
    """Create new review"""
    try:
        data = request.get_json()
        # TODO: Save to database
        return jsonify({
            "success": True,
            "message": "شكراً لتقييمك",
            "review": {}
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "success": False,
        "error": "الصفحة غير موجودة"
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        "success": False,
        "error": "خطأ في الخادم"
    }), 500

# ==================== MAIN ====================

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '0.0.0.0')
    
    print(f"🚗 Auto-Local Palestine")
    print(f"🤖 AI Chatbot {'Enabled ✅' if chatbot_ready else 'Disabled ⚠️'}")
    print(f"🌐 Server running on http://{host}:{port}")
    
    app.run(host=host, port=port, debug=config.DEBUG)
