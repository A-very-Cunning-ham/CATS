// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
//export const prerender = false;
import { images } from "$lib/images";
import type {PageServerLoad} from './$types';

export const load: PageServerLoad = async function() {
	// const data = await images.find({}).toArray();
	// return {
	// 	images: JSON.parse(JSON.stringify(data))
	// }
}