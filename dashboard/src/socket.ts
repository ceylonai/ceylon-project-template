'use client'
import {io} from 'socket.io-client';

// "undefined" means the URL will be computed from the `window.location` object
const URL = process.env.NODE_ENV === 'production' ? 'http://localhost:7878' : 'http://localhost:7878';

export const socket = io(URL, {
    autoConnect: true
});