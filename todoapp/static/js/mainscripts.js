function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function deleteTask(event) {
    const checkbox = event.target;
    const taskId = checkbox.getAttribute('data-id');

    fetch(`/delete/${taskId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        }
    })
    .then(response => {
        if (response.ok) {
            const element = document.getElementById(`todo-${taskId}`);
            element.style.opacity = '0';
            element.style.transition = '0.3s';
            setTimeout(() => element.remove(), 300);
        }
    })
    .catch(error => console.error('Error:', error));
}

document.querySelectorAll('.todo-checkbox').forEach(checkbox => {
    checkbox.addEventListener('change', deleteTask);
});