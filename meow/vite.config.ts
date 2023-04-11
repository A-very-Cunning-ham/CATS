import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';

const config: UserConfig = {
	plugins: [sveltekit()],
	server: {
        host: true,
        port: 8080
    },
    ssr: { noExternal: ['svelte-image-gallery'] }
};

export default config;
