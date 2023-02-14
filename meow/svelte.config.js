import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from '@sveltejs/kit/vite';
import dotenv from "dotenv";
dotenv.config();

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: vitePreprocess({
		replace: [["process.env.URI", process.env.URI]],
	}),

	kit: {
		adapter: adapter()
	}
};

export default config;
