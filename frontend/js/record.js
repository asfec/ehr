document.addEventListener('DOMContentLoaded', () => {
    async function fetchMedicalRecords() {
        try {
            const response = await fetch('http://127.0.0.1:5000/recordrecord'); // Replace with your API URL
            const data = await response.json();

            const alertsDropdown = document.getElementById('alertsDropdown');
            const dropdownList = document.querySelector('.dropdown-list');

            data.forEach(record => {
                const alertItem = document.createElement('a');
                alertItem.className = 'dropdown-item d-flex align-items-center';
                alertItem.href = '#';

                const iconDiv = document.createElement('div');
                iconDiv.className = 'mr-3';

                const iconCircle = document.createElement('div');
                iconCircle.className = 'icon-circle bg-primary';

                const icon = document.createElement('i');
                icon.className = 'fas fa-file-alt text-white';

                iconCircle.appendChild(icon);
                iconDiv.appendChild(iconCircle);

                const textDiv = document.createElement('div');

                const dateDiv = document.createElement('div');
                dateDiv.className = 'small text-gray-500';
                dateDiv.textContent = record.date; // Adjust based on your data structure

                const messageSpan = document.createElement('span');
                messageSpan.className = 'font-weight-bold';
                messageSpan.textContent = record.message; // Adjust based on your data structure

                textDiv.appendChild(dateDiv);
                textDiv.appendChild(messageSpan);

                alertItem.appendChild(iconDiv);
                alertItem.appendChild(textDiv);

                dropdownList.appendChild(alertItem);
            });
        } catch (error) {
            console.error('Error fetching medical records:', error);
        }
    }

    fetchMedicalRecords();
});

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('add-medicalrecord-form');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        const medicalRecordData = {
            patientName: formData.get('patientName'),
            diagnosis: formData.get('diagnosis'),
            treatment: formData.get('treatment'),
            date: formData.get('date'),
            doctorName: formData.get('doctorName')
        };

        try {
            const response = await fetch('http://127.0.0.1:5000/recordrecord', { // Replace with your API URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(medicalRecordData)
            });

            if (response.ok) {
                alert('Medical record added successfully!');
                form.reset();
            } else {
                alert('Failed to add medical record.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while adding the medical record.');
        }
    });
});