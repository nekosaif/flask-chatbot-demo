module.exports = {
    theme: {
      extend: {
        animation: {
          float: 'float 3s ease-in-out infinite',
          pulse: 'pulse 1.5s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        },
        keyframes: {
          float: {
            '0%, 100%': { transform: 'translateY(0)' },
            '50%': { transform: 'translateY(-10px)' },
          }
        }
      }
    }
  }