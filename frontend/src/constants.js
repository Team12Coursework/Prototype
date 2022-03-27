const DEBUG = 1;

const baseURL = DEBUG
    ? "http://localhost:8008"
    // I don't know what the URL of the production server is going to be yet.
    // This will get updated soon.
    : "";

const baseWebSocketURL = DEBUG
    ? "ws://localhost:8008"
    : "";

export { baseURL, baseWebSocketURL };