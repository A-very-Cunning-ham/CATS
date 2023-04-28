import images from "$lib/images";
import { ObjectId } from "mongodb";

export const actions = {
    edit: async ({request}) => {
		const formData = await request.formData()
		console.log(formData)
		
		const idstring = formData.get('id')
		const id = new ObjectId(idstring)
		const age = formData.get('age')
		const weight = formData.get('weight')
		const neutered = formData.get('neutered')
		const note = formData.get('notes')
		
		await images.updateOne(
			{ _id: id },
			{
			$set: {'age': age, 'weight': weight, 'neutered':neutered },
			}
		);

		if(note!=""){
			await images.updateOne(
			{ _id: id },
			{ $push: {'notes': note} }); //creates field if nonexistent
		}
    }
};