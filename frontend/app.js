const API_URL = "YOUR_API_GATEWAY_URL";

async function uploadResume() {
    const file = document.getElementById("resumeFile").files[0];

    const reader = new FileReader();

    reader.onload = async function () {
        const base64 = reader.result.split(",")[1];

        const response = await fetch(API_URL, {
            method: "POST",
            body: JSON.stringify({
                file: base64,
                filename: file.name
            })
        });

        const data = await response.json();

        document.getElementById("result").innerHTML =
            "ATS Score: " + data.score + "%";
    };

    reader.readAsDataURL(file);
}
