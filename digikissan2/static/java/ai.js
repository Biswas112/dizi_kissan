const fileInput = document.getElementById('file-input');
const uploadBox = document.getElementById('upload-box');
const uploadedImage = document.getElementById('uploaded-image');
const scanButton = document.getElementById('scan-button');
const robotScanner = document.getElementById('robot-scanner');
const laserBeam = document.querySelector('.laser-beam');
const resultsSection = document.getElementById('results-section');

fileInput.addEventListener('change', () => {
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            uploadedImage.src = e.target.result;
            uploadedImage.hidden = false;
        };
        reader.readAsDataURL(file);
    }
});

scanButton.addEventListener('click', () => {
    if (!uploadedImage.src) {
        alert('Please upload an image first.');
        return;
    }

    // Display robot and laser
    robotScanner.style.display = 'block';
    laserBeam.style.display = 'block';

    // Start scanning the entire div (simulate a full scan)
    let scanDuration = 6000; // Total duration of the scan (6 seconds)
    let startTime = Date.now();

    // Dynamic position for laser beam based on scan
    let laserPosition = 0;
    let laserInterval = setInterval(() => {
        laserPosition = (Date.now() - startTime) / scanDuration * 100;
        laserBeam.style.left = `${laserPosition}%`;

        if (laserPosition >= 100) {
            clearInterval(laserInterval); // Stop laser movement when scan is complete
        }
    }, 50);

    // Simulate scanning completion
    setTimeout(() => {
        robotScanner.style.display = 'none'; // Hide robot
        laserBeam.style.display = 'none'; // Hide laser

        resultsSection.style.display = 'block'; // Show results

        // Example data (replace with real AI model response)
        document.getElementById('disease-name').textContent = "Powdery Mildew";
        document.getElementById('severity-level').textContent = "Moderate";
        document.getElementById('disease-description').textContent = "A fungal disease that causes white powdery spots.";
        document.getElementById('recommended-actions').textContent = "Use sulfur-based fungicides and ensure proper ventilation.";
    }, scanDuration); // Scanning duration: 6 seconds
});
