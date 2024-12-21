async function fetchCalenderDataAndDisplay() {
    try {
        const response = await fetch('http://127.0.0.1:5000/apointment');
        const data = await response.json();

        const navList = document.querySelector('ul'); 
        data.forEach(item => {
            const listItem = document.createElement('li');
            listItem.className = 'nav-item';

            const link = document.createElement('a');
            link.className = 'nav-link';
            link.href = item.url; 

            const icon = document.createElement('i');
            icon.className = 'fas fa-fw fa-tachometer-alt'; 

            const span = document.createElement('span');
            span.textContent = item.name; 

            link.appendChild(icon);
            link.appendChild(span);
            listItem.appendChild(link);
            navList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Call the function to fetch data and display it
fetchCalenderDataAndDisplay();

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('add-calender-event-form');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        const eventData = {
            title: formData.get('patient_id'),
            date: formData.get('date'),
            time: formData.get('time'),
            description: formData.get('description')
        };

        try {
            const response = await fetch('http://127.0.0.1:5000/apointment ', { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(eventData)
            });

            if (response.ok) {
                alert('Event added successfully!');
                form.reset();
            } else {
                alert('Failed to add event.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while adding the event.');
        }
    });
});