const token = document.getElementById('token-user-id-data').getAttribute('data-token');
const user_id = document.getElementById('token-user-id-data').getAttribute('data-user-id');
const userName = document.getElementById('token-user-id-data').getAttribute('user');
const channelname = document.getElementById('token-user-id-data').getAttribute('data-room-id');
room_id = document.getElementById('token-user-id-data').getAttribute('room-id');

const APP_ID = 'f055d16d5cb9403493bf2f68ba29d67a';
const CHANNEL = channelname;
const TOKEN = token
UID = user_id;

const client = AgoraRTC.createClient({ mode: 'rtc', codec: 'vp8' });
let localTrack = []
let remoteUser = {}

const joinAndDisplayLocalStream = async () => {
    client.on('user-published', handelUserJoin)
    client.on('user-left', handelUserLeft)

    await client.join(APP_ID, CHANNEL, TOKEN, UID);
    localTrack = await AgoraRTC.createMicrophoneAndCameraTracks();

    let player = `<div class="user-video">
                    <div class="video-container">
                        <video id="user-${UID}"></video>
                    </div>
                    <div class="user-details">
                    <div class="user-name">${userName}</div>
                    <div class="user-role"></div>
                    </div>
                </div>`

    document.querySelector('.conference-container').insertAdjacentHTML('beforeend', player);

    localTrack[1].play(`user-${UID}`);

    client.publish(localTrack);
}

let handelUserJoin = async (user, mediaType) =>{
    remoteUser[user.uid] = user

    await client.subscribe(user, mediaType)
    if (mediaType==='video'){
        let player = document.getElementById(`video-container-${user.uid}`)
        if (player != null){
            player.remove()
        }
      
      player =  `<div class="user-video" id="video-container-${user.uid}">
                <div class="video-container">
                    <video id="user-${user.uid}"></video>
                </div>
                <div class="user-details">
                <div class="user-name">😍😁😊</div>
                <div class="user-role"></div>
                </div>
                </div>`;
        
document.querySelector('.conference-container').insertAdjacentHTML('beforeend', player);
user.videoTrack.play(`user-${user.uid}`)

    }
    if (mediaType==='audio'){
        user.audioTrack.play()
    }
}

let handelUserLeft = async (user) => {
    delete remoteUser[user.uid]
    document.getElementById(`video-container-${user.uid}`).remove()
}

document.getElementById('end-call-button').addEventListener('click', leaveAndRemoveLocalstream);
document.getElementById('close-camera-button').addEventListener('click', toggleCamera);
document.getElementById('mute-button').addEventListener('click', toggleMic);
async function leaveAndRemoveLocalstream() {
    for (let i = 0; i < localTrack.length; i++) {
        await localTrack[i].stop(); // Stop each individual track
        await localTrack[i].close(); // Close each individual track
    }

    await client.leave();
    window.open('/chat/leave-video-stream/' + room_id, '_self');
}

async function toggleCamera (e) {
    const iconElement = e.currentTarget.querySelector('i');
    if (localTrack[1].muted){
        await localTrack[1].setMuted(false)
        iconElement.className = 'fas fa-camera';
    }else {
        await localTrack[1].setMuted(true)
        iconElement.className = 'fa-solid fa-lock';;
    }
}

async function toggleMic (e) {
    const iconElement = e.currentTarget.querySelector('i');
    if (localTrack[0].muted){
        await localTrack[0].setMuted(false)
        iconElement.className ='fa-solid fa-microphone-lines';
    }else {
        await localTrack[0].setMuted(true)
        iconElement.className = 'fas fa-microphone-slash';
    }
}
joinAndDisplayLocalStream();


