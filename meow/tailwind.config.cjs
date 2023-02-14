/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{svelte,js,ts,jsx,tsx}",
    "./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}"
  ],
  theme: {
    extend: {},
  },
  plugins: ['flowbite/plugin'],
}
