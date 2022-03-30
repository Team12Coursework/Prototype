const DEBUG = 1;

const baseURL = DEBUG
    ? "http://localhost:8000"
    // I don't know what the URL of the production server is going to be yet.
    // This will get updated soon.
    : "";

const baseWebSocketURL = DEBUG
//The secure wss:// protocol has been used over ws:// as ws:// is an insecure method of transport
//WSS is encrpyted and provides protection against man-in-the-middle-attacks, therefore is more safer to use
//As the transport is secured using this protocol, it protects the websockets from multiple types of attacks
    ? "wss://localhost:8000"
    : "";

export { baseURL, baseWebSocketURL };