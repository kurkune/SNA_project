<script>
	let text_e = ''
	let text_d = ''

	async function handleSubmit() {
		const request = await fetch('https://SNAproject.pythonanywhere.com/encode', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'Allow-Control-Allow-Origin': '*'
			},
			body: JSON.stringify({ text: text_e })
		})

		if (!request.ok) {
			const message = `An error has occured: ${request.status}`
			throw new Error(message)
		}

		const data = await request.json()
		console.log(data)
	}

	async function handle() {
		const request = await fetch('https://SNAproject.pythonanywhere.com/decode', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'Allow-Control-Allow-Origin': '*'
			},
			body: JSON.stringify({ text: text_d })
		})

		if (!request.ok) {
			const message = `An error has occured: ${request.status}`
			throw new Error(message)
		}

		const data = await request.json()
		console.log(data)
	}
</script>

<div class="navbar bg-base-100">
	<div class="flex-none">
		<div class="drawer z-50">
			<input id="my-drawer" type="checkbox" class="drawer-toggle" />
			<div class="drawer-content">
				<label for="my-drawer" class="btn btn-square btn-ghost drawer-button">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						class="inline-block w-5 h-5 stroke-current"
						><path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M4 6h16M4 12h16M4 18h16"
						></path></svg
					>
				</label>
			</div>
			<div class="drawer-side">
				<label for="my-drawer" aria-label="close sidebar" class="drawer-overlay"></label>
				<ul class="menu p-4 w-80 min-h-full bg-base-200 text-base-content">
					<li>Sidebar Item 1</li>
					<li>Sidebar Item 2</li>
				</ul>
			</div>
		</div>
	</div>
	<div class="flex-1"></div>
	<div class="flex-none">
		<label class="flex cursor-pointer gap-2">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="20"
				height="20"
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
				stroke-linecap="round"
				stroke-linejoin="round"
				><circle cx="12" cy="12" r="5" /><path
					d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"
				/></svg
			>
			<input type="checkbox" value="dark" class="toggle theme-controller" />
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="20"
				height="20"
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
				stroke-linecap="round"
				stroke-linejoin="round"
				><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg
			>
		</label>
	</div>
</div>

<div class="kaif">
	<div class="mx-auto max-w-7xl py-24 sm:px-6 sm:py-16 lg:px-8">
		<div
			class="relative isolate overflow-hiddenpx-6 pt-8 sm:rounded-3xl sm:px-16 md:pt-24 lg:flex lg:gap-x-20 lg:px-24 lg:pt-0"
		>
			<div class="mx-auto max-w-md text-center lg:mx-0 lg:flex-auto lg:py-32 lg:text-left">
				<h2 class="text-3xl font-bold tracking-tight sm:text-4xl">
					Encode and Decode your text into emoji
				</h2>
				<p class="mt-6 text-lg leading-8">
					Write any message using the code words displayed in the SideBar
				</p>
				<div class="mt-10 flex items-center justify-center gap-x-6 lg:justify-start">
					<a href="#start" class="text-md font-semibold leading-6 underline"
						>Get started<span aria-hidden="true">→</span></a
					>
				</div>
			</div>
			<div class="relative ml-16 mt-16 h-80 lg:mt-8">
				<img
					class="w-[25rem] max-w-none"
					src="src/lib/components/Smiling face with heart-eyes.svg"
					alt="emoji"
				/>
			</div>
		</div>
	</div>
</div>

<div id="start" class="lg:pt-16 text-center">
	<h1 class="text-4xl font-bold">Encode and Decode your text into emojis</h1>
</div>
<div class="lg:py-8 text-center">
	<form on:submit|preventDefault={handleSubmit}>
		<input
			bind:value={text_e}
			type="text"
			placeholder="Type here"
			class="input input-bordered input-accent w-full max-w-xs"
		/>
		<button type="submit" class="btn btn-accent mt-4">Submit</button>
	</form>
</div>

<div class="lg:py-8 text-center">
	<form on:submit|preventDefault={handle}>
		<input
			bind:value={text_d}
			type="text"
			placeholder="Type here"
			class="input input-bordered input-accent w-full max-w-xs"
		/>
		<button type="submit" class="btn btn-accent mt-4">Submit</button>
	</form>
</div>
