//function for csrf token. from django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const notification_buttons = document.querySelectorAll('.notifications-container button');

notification_buttons.forEach( button =>{
    button.addEventListener('click',()=>{
        const faq = button.nextElementSibling;
        const icon = button.children[1];

        faq.classList.toggle('show');
        icon.classList.toggle('rotate');
    })
} )
// function for marking as read
let btn = document.querySelectorAll(".notification button")
btn.forEach(btn=>{
    btn.addEventListener("click", mark_read)
})

async function mark_read(e) {
    let question_id = e.target.getAttribute("value");
    let url = "/notification/mark_read";  // Replace with your backend URL
    let data = { id: question_id };
    
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', 'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            console.log("Notification marked as read");
            // You can add further actions here if needed
        } else {
            console.error('Failed to mark notification as read');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}





// function for dropdown of notification
const buttons = document.querySelectorAll('button');

buttons.forEach( button =>{
    button.addEventListener('click',()=>{
        const faq = button.nextElementSibling;
        const icon = button.children[1];
    })
} )

