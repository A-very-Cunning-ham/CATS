// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
//export const prerender = false;
import images from "$lib/images";
import type {PageServerLoad, Actions} from './$types';

export const actions: Actions = { 
	default: async ({ request }) => {
		const formData = await request.formData();
		console.log(formData)
		const data = {};

		for (let field of formData) {
			const [key, value] = field;
			data[key] = value;
		}

		data["type"] = "cat"
		data["events"] = [data['events']]

		const result = await images.insertOne(data);
	
		console.log('New cat added: ', data['name']);
		console.log(result);
		return {
		  success: true,
		};
	  }
}

export const load: PageServerLoad = async function() {
	const data = await images.find({}).sort({_id: -1}).toArray();
	return {
		images: JSON.parse(JSON.stringify(data)) 
	}
}