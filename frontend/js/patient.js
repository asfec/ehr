async function fetchPatientDataAndDisplay() {
    try {
        const response = await fetch('http://127.0.0.1:5000/patient'); 
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

fetchPatientDataAndDisplay();

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('add-patient-form');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        const patientData = {
            name: formData.get('name'),
            age: formData.get('age'),
            gender: formData.get('gender'),
            phone: formData.get('phone'),
            email: formData.get('email')
        };

        try {
            const response = await fetch('http://127.0.0.1:5000/patient', { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(patientData)
            });

            if (response.ok) {
                alert('Patient added successfully!');
                form.reset();
            } else {
                alert('Failed to add patient.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while adding the patient.');
        }
    });
});
