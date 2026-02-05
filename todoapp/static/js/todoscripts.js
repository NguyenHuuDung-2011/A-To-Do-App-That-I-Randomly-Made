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

document.getElementById('addTask').addEventListener('click', function(event) {
    event.preventDefault();

    const title = document.querySelector('input[name="title"]').value;
    const description = document.querySelector('input[name="description"]').value;
    const deadlineDate = document.querySelector('input[name="deadline_date"]').value;

    const formData = new FormData();
    formData.append('title', title);
    formData.append('description', description);
    formData.append('deadline_date', deadlineDate);

    fetch('/add/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData
    })
    .then(response => {
        if (response.ok) {
            location.reload();
        }
    })
    .catch(error => console.error('Error:', error));
})

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