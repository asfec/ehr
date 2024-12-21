async function fetchDataAndDisplay() {
    try {
        const response = await fetch('http://127.0.0.1:5000/doctor');
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
            span.textContent = item.name; // 

            link.appendChild(icon);
            link.appendChild(span);
            listItem.appendChild(link);
            navList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

fetchDataAndDisplay();


// them bac si
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('add-doctor-form');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        const doctorData = {
            name: formData.get('name'),
            specialty: formData.get('specialty'),
            phone: formData.get('phone'),
            email: formData.get('email')
        };

        try {
            const response = await fetch('http://127.0.0.1:5000/doctor', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(doctorData)
            });

            if (response.ok) {
                alert('Doctor added successfully!');
                form.reset();
            } else {
                alert('Failed to add doctor.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while adding the doctor.');
        }
    });
});

//lay chi tiet bac si 