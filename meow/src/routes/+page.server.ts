// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
//export const prerender = false;
import { images, cats } from "$lib/images";
import type {PageServerLoad} from './$types';

export const load: PageServerLoad = async function() {
	const data = await images.find({}).sort({_id: -1}).toArray();
	const data2 = await cats.find({}).sort({_id: -1}).toArray();
	return {
		images: JSON.parse(JSON.stringify(data)),
		cats: JSON.parse(JSON.stringify(data2))
	}
}