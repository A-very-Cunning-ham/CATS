import db from '$lib/mongo'

export const images = db.collection('images')
export const cats = db.collection('cats')