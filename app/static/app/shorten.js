document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('shortener-form').addEventListener('submit', async function(e) {
        e.preventDefault();
        const longUrl = document.getElementById('long-url').value;
        const customUrl = document.getElementById('custom-short-url').value;
        try {
            // Get the CSRF token from the form
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const response = await fetch('api/shorten_url/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ url: longUrl, custom_url: customUrl }),
            });
            
            const data = await response.json();
            if (response.ok) {
                const resultDiv = document.getElementById('result');
                const shortUrlLink = document.getElementById('short-url-link');
                
                shortUrlLink.href = data.short_url;
                shortUrlLink.textContent = data.short_url;
                resultDiv.classList.remove('hidden');
            } else {
                alert('Error: ' + data.error);
            }
        } catch (error) {
            alert('An error occurred. Please try again.');
        }
    });
});