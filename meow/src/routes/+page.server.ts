// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
//export const prerender = false;
import images from "$lib/images";
import type {PageServerLoad, Actions} from './$types';

export const actions: Actions = { 
	create: async ({ request }) => {
		const formData = await request.formData();
		
		const data = {};

		for (let field of formData) {
			const [key, value] = field;
			data[key] = value;
		}

		const result = await images.insertOne(data);
	
		console.log('New cat added: ', data['name']);
		return {
		  success: true,
		};
	  }
	//   update: async ({ request }) => {
	// 	const formData = await request.formData();
	// 	const todoId = formData.get('todoId');
	// 	const todoName = formData.get('todoName');
	// 	await dbConnect();
	// 	await TodoModel.findByIdAndUpdate(todoId, {
	// 	  title: todoName,
	// 	}).lean();
	// 	await dbDisconnect();
	
	// 	console.log('Todo updated: ', todoId);
	
	// 	return {
	// 	  success: true,
	// 	};
	//   }
}

export const load: PageServerLoad = async function() {
	const data = await images.find({}).sort({_id: -1}).toArray();
	return {
		images: JSON.parse(JSON.stringify(data)) 
	}
}