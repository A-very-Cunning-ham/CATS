import { invalidateAll } from '$app/navigation';
import type {PageServerLoad} from './$types';
import images from "$lib/images";

export const dateFromObjectId = function (objectId) {
    return new Date(parseInt(objectId.substring(0, 8), 16) * 1000).toLocaleString('en-US', { timeZone: 'UTC' });
};

export const restart = function() {
    invalidateAll();
}

// mongo_type: String, 'image' or 'cat'
export const load_cats: PageServerLoad = async function(mongo_type) {
    const data = await images.find({'type': mongo_type}).sort({_id: -1}).toArray();
    return {
        images: JSON.parse(JSON.stringify(data))
    }
}
