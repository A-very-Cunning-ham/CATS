// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
//export const prerender = false;
import images from "$lib/images";
import { ObjectId } from "mongodb";
import type {PageServerLoad, Actions} from './$types';

export const load: PageServerLoad = async function() {
	const data = await images.find({'type':'cat'}).sort({_id: -1}).toArray();
	
	return {
		images: JSON.parse(JSON.stringify(data)),

	}
};

export const actions = {
    create: async ({request}) => {
		const formData = await request.formData();
		console.log(formData);
		const doc = {
			type: "cat",
			events: [[new ObjectId]],
			name: formData.get('name'),
			age: formData.get('age'),
			weight: formData.get('weight'),
			neutered: formData.get('neutered')
		}
		const out = await images.insertOne(doc);
		// console.log(out);
    },

	delete: async ({ request }) => {
		const formData = await request.formData()
		const id = formData.get('id')
		
		const out = await images.deleteOne({_id:new ObjectId({id})}); //its not null, its a string but it cant tell in the context of this function

		console.log(id)
	}
};