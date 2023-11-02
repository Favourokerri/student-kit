const APP_ID = 'f055d16d5cb9403493bf2f68ba29d67a';
const CHANNEL = 'main';
const TOKEN = '007eJxTYDjeMfFlu10yx1y9WqV8hTPHft75sWeP3XyGae6TdullsloqMKQZmJqmGJqlmCYnWZoYGJtYGielGaWZWSQlGlmmmJknZv53Sm0IZGSYHuLIzMgAgSA+C0NuYmYeAwMAWPMfOw==';
let UID;

const client = AgoraRTC.createClient({ mode: 'rtc', codec: 'vp8' });
let localTrack = [];

const joinAndDisplayLocalStream = async () => {
    client.on('user-published', (user, mediaType) => {
        console.log('A user has joined our stream');
    });

    UID = await client.join(APP_ID, CHANNEL, TOKEN, null);
    localTrack = await AgoraRTC.createMicrophoneAndCameraTracks();

    let player = ` <div class="video-container" id="video-container-${UID}">
                    <video id="user-${UID}"></video>
                </div>`;
    document.querySelector('.stream').insertAdjacentHTML('beforeend', player);

    localTrack[1].play(`user-${UID}`);

    client.publish(localTrack);
}

joinAndDisplayLocalStream();