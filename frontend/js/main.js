/**
 * Main JavaScript - General utilities and helpers
 */

// API Configuration
const API_CONFIG = {
    BASE_URL: '/api',
    TIMEOUT: 10000
};

// Utility Functions
const Utils = {
    /**
     * Make API call
     */
    async apiCall(endpoint, options = {}) {
        try {
            const url = `${API_CONFIG.BASE_URL}${endpoint}`;
            const response = await fetch(url, {
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                },
                ...options
            });
            
            if (!response.ok) {
                throw new Error(`API Error: ${response.statusCode}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('API Call Error:', error);
            throw error;
        }
    },
    
    /**
     * Format price
     */
    formatPrice(price) {
        return `₪ ${price.toFixed(2)}`;
    },
    
    /**
     * Format date
     */
    formatDate(date) {
        return new Date(date).toLocaleDateString('ar-PS', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    },
    
    /**
     * Show notification
     */
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    },
    
    /**
     * Get user location
     */
    getUserLocation() {
        return new Promise((resolve, reject) => {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    position => {
                        resolve({
                            lat: position.coords.latitude,
                            lon: position.coords.longitude
                        });
                    },
                    error => reject(error)
                );
            } else {
                reject(new Error('Geolocation not supported'));
            }
        });
    }
};

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚗 Auto-Local Palestine App Initialized');
    initializeApp();
});

function initializeApp() {
    // Check health
    Utils.apiCall('/health')
        .then(response => {
            console.log('✅ Server is healthy:', response);
        })
        .catch(error => {
            console.error('❌ Server connection error:', error);
        });
}

// Export utilities
window.Utils = Utils;
