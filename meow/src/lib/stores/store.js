// src/store.js

import { writable, derived, readable } from "svelte/store";


export const isAuthenticated = writable(false);
export const user = writable({});
export const cat = writable({});
export const popupOpen = writable(false);
export const error = writable();

export const time = readable(new Date(), function start(set) {
	const interval = setInterval(() => {
		set(new Date());
	}, 1000);

	return function stop() {
		clearInterval(interval);
	};
});