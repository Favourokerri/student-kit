document.addEventListener("DOMContentLoaded", function() {
    let speech_btn = document.querySelectorAll(".card-footer button");
    speech_btn.forEach(speech_btn => {
        speech_btn.addEventListener("click", speech);
    });

    async function speech(e) {
        let card_id = e.currentTarget.getAttribute("data-card-id");
        console.log("executing speech");
        let url = "/flashcards/text_to_speech/";
        let data = { id: card_id };

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify(data),
            }); 
            if (response.ok) {
                //get title from backend and turn to speech
                const responseData = await response.json();
                const question = responseData.question;
                const synth = window.speechSynthesis;
                const utterance = new SpeechSynthesisUtterance(question);
                synth.speak(utterance);
                console.log("executed successfully");

            } else {
                console.error('failed to read text');
            }
        } catch (error) {
            console.error('ERROR:', error);
        }
    }
});