<script>
	import { page } from '$app/stores';
	import github from '$lib/images/github.svg';
</script>

<footer class="flex justify-between items-center p-3">
	<div class="corner">
		<a href="https://github.com/A-very-Cunning-ham/CATS/tree/main" target="_blank" rel="noreferrer noopener" class="flex items-center justify-center w-full h-full"> 
			<img src={github} alt="GitHub" class="object-contain" />
		</a>
	</div>

	<!-- <p>visit <a href="https://sit.instructure.com/courses/65029" target="_blank" rel="noreferrer noopener" class="font-bold">canvas</a> to view the senior design course</p> -->

    <div class="corner"/>
</footer>

<style>
    .corner {
        width: 3em;
		height: 3em;
	}

	.corner img {
		width: 2em;
		height: 2em;
		object-fit: contain;
	}

    @media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
