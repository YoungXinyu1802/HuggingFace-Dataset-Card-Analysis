<!DOCTYPE html>
<html class="">
	<head>
		<meta charset="utf-8" />
		<meta
			name="viewport"
			content="width=device-width, initial-scale=1.0, user-scalable=no"
		/>
		<meta name="description" content="We’re on a journey to advance and democratize artificial intelligence through open source and open science." />
		<meta property="fb:app_id" content="1321688464574422" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:site" content="@huggingface" />
		<meta property="og:title" content="README.md · lewtun/github-issues at main" />
		<meta property="og:type" content="website" />
		<meta property="og:url" content="https://huggingface.co/datasets/lewtun/github-issues/blob/main/README.md" />
		<meta property="og:image" content="https://huggingface.co/front/thumbnails/v2-2.png" />

		<link rel="stylesheet" href="/front/build/style.6509d170.css" />

		<link rel="preconnect" href="https://fonts.gstatic.com" />
		<link
			href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap"
			rel="stylesheet"
		/>
		<link
			href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap"
			rel="stylesheet"
		/>
		<link
			rel="stylesheet"
			href="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.min.css"
		/>

		 

		<title>README.md · lewtun/github-issues at main</title>
	</head>
	<body
		class="flex flex-col min-h-screen bg-white dark:bg-gray-950 text-black ViewerBlobPage"
	>
		<div class="flex flex-col min-h-screen "><header class="border-b border-gray-100"><div class="w-full px-4 lg:px-6 xl:container flex items-center h-16"><div class="flex flex-1 items-center"><a class="flex flex-none items-center mr-5 lg:mr-6" href="/"><img alt="Hugging Face's logo" class="md:mr-2 w-7" src="/front/assets/huggingface_logo-noborder.svg">
				<span class="hidden text-lg font-bold whitespace-nowrap md:block">Hugging Face</span></a>
			
			<div class="SVELTE_HYDRATER contents" data-props="{&quot;classNames&quot;:&quot;flex-1 lg:max-w-sm mr-2 sm:mr-4 lg:mr-6&quot;,&quot;header&quot;:true,&quot;placeholder&quot;:&quot;Search models, datasets, users...&quot;,&quot;url&quot;:&quot;/api/quicksearch&quot;,&quot;searchParams&quot;:{&quot;withLinks&quot;:true}}" data-target="QuickSearch"><div class="relative flex-1 lg:max-w-sm mr-2 sm:mr-4 lg:mr-6"><input autocomplete="off" class="w-full dark:bg-gray-950 
			form-input-alt h-9 pl-8 pr-3 focus:shadow-xl" name="" placeholder="Search models, datasets, users..."  spellcheck="false" type="text">
	<svg class="absolute left-2.5 top-2.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9a9 9 0 0 1-9-9z" fill="currentColor"></path></svg>
	</div></div>
			<div class="SVELTE_HYDRATER contents" data-props="{&quot;apiInferenceUrl&quot;:&quot;https://api-inference.huggingface.co&quot;}" data-target="NavigationMenuPhone"><button class="lg:hidden relative flex-none place-self-stretch flex items-center justify-center w-8" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="22" height="22" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M4 24h24v2H4z"></path><path d="M4 12h24v2H4z"></path><path d="M4 18h24v2H4z"></path><path d="M4 6h24v2H4z"></path></svg></button>
</div></div>
		<div class="SVELTE_HYDRATER contents" data-props="{&quot;apiInferenceUrl&quot;:&quot;https://api-inference.huggingface.co&quot;,&quot;hfCloudName&quot;:&quot;private&quot;,&quot;isAuth&quot;:false,&quot;isHfCloud&quot;:false}" data-target="NavigationMenuDesktop"><nav aria-label="Main" class="ml-auto hidden lg:block"><ul class="flex items-center space-x-2"><li><a class="flex items-center group px-2 py-0.5 dark:hover:text-gray-400 hover:text-indigo-700" href="/models"><svg class="mr-1.5 text-gray-400 group-hover:text-indigo-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
					Models</a>
			</li><li><a class="flex items-center group px-2 py-0.5 dark:hover:text-gray-400 hover:text-red-700" href="/datasets"><svg class="mr-1.5 text-gray-400 group-hover:text-red-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
					Datasets</a>
			</li><li><a class="flex items-center group px-2 py-0.5 dark:hover:text-gray-400 hover:text-blue-700" href="/spaces"><svg class="mr-1.5 text-gray-400 group-hover:text-blue-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 25 25"><path opacity=".5" d="M6.016 14.674v4.31h4.31v-4.31h-4.31ZM14.674 14.674v4.31h4.31v-4.31h-4.31ZM6.016 6.016v4.31h4.31v-4.31h-4.31Z" fill="currentColor"></path><path opacity=".75" fill-rule="evenodd" clip-rule="evenodd" d="M3 4.914C3 3.857 3.857 3 4.914 3h6.514c.884 0 1.628.6 1.848 1.414a5.171 5.171 0 0 1 7.31 7.31c.815.22 1.414.964 1.414 1.848v6.514A1.914 1.914 0 0 1 20.086 22H4.914A1.914 1.914 0 0 1 3 20.086V4.914Zm3.016 1.102v4.31h4.31v-4.31h-4.31Zm0 12.968v-4.31h4.31v4.31h-4.31Zm8.658 0v-4.31h4.31v4.31h-4.31Zm0-10.813a2.155 2.155 0 1 1 4.31 0 2.155 2.155 0 0 1-4.31 0Z" fill="currentColor"></path><path opacity=".25" d="M16.829 6.016a2.155 2.155 0 1 0 0 4.31 2.155 2.155 0 0 0 0-4.31Z" fill="currentColor"></path></svg>
					Spaces</a>
			</li><li><a class="flex items-center group px-2 py-0.5 dark:hover:text-gray-400 hover:text-yellow-700" href="/docs"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1.5 text-gray-400 group-hover:text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path opacity="0.5" d="M20.9022 5.10334L10.8012 10.8791L7.76318 9.11193C8.07741 8.56791 8.5256 8.11332 9.06512 7.7914L15.9336 3.73907C17.0868 3.08811 18.5002 3.26422 19.6534 3.91519L19.3859 3.73911C19.9253 4.06087 20.5879 4.56025 20.9022 5.10334Z" fill="currentColor"></path><path d="M10.7999 10.8792V28.5483C10.2136 28.5475 9.63494 28.4139 9.10745 28.1578C8.5429 27.8312 8.074 27.3621 7.74761 26.7975C7.42122 26.2327 7.24878 25.5923 7.24756 24.9402V10.9908C7.25062 10.3319 7.42358 9.68487 7.74973 9.1123L10.7999 10.8792Z" fill="currentColor" fill-opacity="0.75"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M21.3368 10.8499V6.918C21.3331 6.25959 21.16 5.61234 20.8346 5.03949L10.7971 10.8727L10.8046 10.874L21.3368 10.8499Z" fill="currentColor"></path><path opacity="0.5" d="M21.7937 10.8488L10.7825 10.8741V28.5486L21.7937 28.5234C23.3344 28.5234 24.5835 27.2743 24.5835 25.7335V13.6387C24.5835 12.0979 23.4365 11.1233 21.7937 10.8488Z" fill="currentColor"></path></svg>
					Docs</a>
			</li>
		<li><div class="relative ">
	<button class="px-2 py-0.5 group hover:text-green-700 dark:hover:text-gray-400 flex items-center
			" type="button">
		<svg class="mr-1.5 text-gray-400 group-hover:text-green-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M19 6H5a3 3 0 0 0-3 3v2.72L8.837 14h6.326L22 11.72V9a3 3 0 0 0-3-3z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M10 6V5h4v1h2V5a2.002 2.002 0 0 0-2-2h-4a2.002 2.002 0 0 0-2 2v1h2zm-1.163 8L2 11.72V18a3.003 3.003 0 0 0 3 3h14a3.003 3.003 0 0 0 3-3v-6.28L15.163 14H8.837z" fill="currentColor"></path></svg>
			Solutions
			</button>
	
	
	
	</div></li>

			<li><a class="flex items-center group px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-400" href="/pricing" data-ga-category="header-menu" data-ga-action="clicked pricing" data-ga-label="pricing">Pricing
				</a></li>

		<li><div class="relative group">
	<button class="px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-600 flex items-center
			" type="button">
		<svg class="mr-1.5 text-gray-500 w-5 group-hover:text-gray-400 dark:text-gray-300 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 18" preserveAspectRatio="xMidYMid meet"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 3.30221C14.4504 2.836 14.8284 2.45807 15.2946 2.45807H28.4933C28.9595 2.45807 29.3374 2.836 29.3374 3.30221C29.3374 3.76842 28.9595 4.14635 28.4933 4.14635H15.2946C14.8284 4.14635 14.4504 3.76842 14.4504 3.30221Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 9.00002C14.4504 8.53382 14.8284 8.15588 15.2946 8.15588H28.4933C28.9595 8.15588 29.3374 8.53382 29.3374 9.00002C29.3374 9.46623 28.9595 9.84417 28.4933 9.84417H15.2946C14.8284 9.84417 14.4504 9.46623 14.4504 9.00002Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 14.6978C14.4504 14.2316 14.8284 13.8537 15.2946 13.8537H28.4933C28.9595 13.8537 29.3374 14.2316 29.3374 14.6978C29.3374 15.164 28.9595 15.542 28.4933 15.542H15.2946C14.8284 15.542 14.4504 15.164 14.4504 14.6978Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.94549 6.87377C2.27514 6.54411 2.80962 6.54411 3.13928 6.87377L6.23458 9.96907L9.32988 6.87377C9.65954 6.54411 10.194 6.54411 10.5237 6.87377C10.8533 7.20343 10.8533 7.73791 10.5237 8.06756L6.23458 12.3567L1.94549 8.06756C1.61583 7.73791 1.61583 7.20343 1.94549 6.87377Z" fill="currentColor"></path></svg>
			
			</button>
	
	
	
	</div></li>
		<li><hr class="w-0.5 h-5 border-none bg-gray-100 dark:bg-gray-800"></li>
		
			<li><a class="px-2 py-0.5 block cursor-pointer hover:text-gray-500 dark:hover:text-gray-400" href="/login">Log In
				</a></li>
			<li><a class="ml-2 btn" href="/join">Sign Up </a></li></ul></nav></div></div></header>
	
	
	<main class="flex flex-col flex-1 "><header class="bg-gradient-to-t from-gray-50-to-white via-white dark:via-gray-950 
		pt-10 "><div class="container relative"><h1 class="flex items-center flex-wrap text-lg leading-tight 
				mb-2 md:text-xl "><a href="/datasets" class="group flex items-center mb-1"><svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
					<span class="text-gray-400 group-hover:text-gray-500 mr-3 font-semibold">Datasets:</span></a>
			<div class="flex items-center mb-1"><img alt="Lewis Tunstall's avatar" class="w-4 h-4 rounded-full mr-1.5" src="https://aeiljuispo.cloudimg.io/v7/https://s3.amazonaws.com/moonup/production/uploads/1594651707950-noauth.jpeg?w=200&amp;h=200&amp;f=face">
					<a href="/lewtun" class="font-sans text-gray-400 hover:text-blue-600">lewtun</a>
					<div class="text-gray-300 mx-0.5">/</div></div>
			<div class="max-w-full mb-1"><a class="font-mono font-semibold break-words" href="/datasets/lewtun/github-issues">github-issues</a>
				<div class="SVELTE_HYDRATER contents" data-props="{&quot;classNames&quot;:&quot;mr-4&quot;,&quot;title&quot;:&quot;Copy dataset name to clipboard&quot;,&quot;value&quot;:&quot;lewtun/github-issues&quot;}" data-target="CopyButton"><button class="inline-flex items-center relative bg-white text-sm focus:text-green-500  cursor-pointer focus:outline-none
		mr-4
		mx-0.5
		
		
		text-gray-600
		
	" title="Copy dataset name to clipboard" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	<div class="
		absolute pointer-events-none transition-opacity bg-black text-white py-1 px-2 leading-tight rounded font-normal shadow 
		left-1/2 top-full transform -translate-x-1/2 translate-y-2
		opacity-0
	"><div class="absolute bottom-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-black border-4 border-t-0" style="
				border-left-color: transparent;
				border-right-color: transparent;
			"></div>
	Copied</div></button></div></div>
			<div class="SVELTE_HYDRATER contents" data-props="{&quot;classNames&quot;:&quot;mr-3 mb-1&quot;,&quot;isLikedByUser&quot;:false,&quot;likes&quot;:1,&quot;repoId&quot;:&quot;lewtun/github-issues&quot;,&quot;repoType&quot;:&quot;dataset&quot;}" data-target="LikeButton"><div class="inline-flex items-center border leading-none whitespace-nowrap text-sm rounded-md text-gray-500 overflow-hidden bg-white
		 mr-3 mb-1"><button class="relative flex items-center px-1.5 py-1 hover:bg-gradient-to-t focus:outline-none from-red-50 to-transparent dark:from-red-900 dark:to-red-800 overflow-hidden"  title="Like"><svg class="mr-1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z"></path></svg>

		<svg class="mr-1 absolute text-red-500 origin-center transform transition ease-in\n\t\t\t\ttranslate-y-10 scale-0" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.5,4c-2,0-3.9,0.8-5.3,2.2L16,7.4l-1.1-1.1C12,3.3,7.2,3.3,4.3,6.2c0,0-0.1,0.1-0.1,0.1c-3,3-3,7.8,0,10.8L16,29l11.8-11.9c3-3,3-7.8,0-10.8C26.4,4.8,24.5,4,22.5,4z"></path></svg>
		like
	</button>
	<button class="flex items-center px-1.5 py-1 border-l text-gray-400 focus:outline-none hover:bg-gray-50 dark:hover:bg-gray-700 focus:bg-gray-100 " title="See users who liked this repository">1</button></div>
</div>
			</h1>
		<div class="flex flex-wrap mb-3 lg:mb-5"></div>
		<div class="border-b border-gray-100"><div class="flex flex-col-reverse lg:flex-row lg:items-center lg:justify-between"><div class="flex items-center h-12 -mb-px overflow-x-auto overflow-y-hidden"><a class="tab-alternate " href="/datasets/lewtun/github-issues"><svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
				Dataset card
			</a>
			<a class="tab-alternate active" href="/datasets/lewtun/github-issues/tree/main"><svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M21 19h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-8h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0 4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M9 19a1 1 0 0 1-1-1V6a1 1 0 0 1 2 0v12a1 1 0 0 1-1 1zm-6-4.333a1 1 0 0 1-.64-1.769L3.438 12l-1.078-.898a1 1 0 0 1 1.28-1.538l2 1.667a1 1 0 0 1 0 1.538l-2 1.667a.999.999 0 0 1-.64.231z" fill="currentColor"></path></svg>
				Files and versions
			</a>
			
			</div>
	
				</div></div></div></header>
	
<div class="container relative flex flex-col md:grid md:space-y-0 w-full
	md:grid-cols-12
	 
		space-y-4
		md:gap-6
		mb-16
	"><section class="pt-8 border-gray-100 col-span-full"><header class="pb-2 flex items-center justify-between flex-wrap"><div class="flex flex-wrap items-center"><div class="SVELTE_HYDRATER contents" data-props="{&quot;path&quot;:&quot;README.md&quot;,&quot;repoName&quot;:&quot;lewtun/github-issues&quot;,&quot;repoType&quot;:&quot;dataset&quot;,&quot;rev&quot;:&quot;main&quot;,&quot;refs&quot;:{&quot;branches&quot;:[&quot;main&quot;],&quot;tags&quot;:[]},&quot;view&quot;:&quot;blob&quot;}" data-target="BranchSelector"><div class="relative mr-4 mb-2">
	<button class="text-base
			cursor-pointer w-full btn text-sm" type="button">
		<svg class="mr-1.5 text-gray-700 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M13 14c-3.36 0-4.46 1.35-4.82 2.24C9.25 16.7 10 17.76 10 19a3 3 0 0 1-3 3a3 3 0 0 1-3-3c0-1.31.83-2.42 2-2.83V7.83A2.99 2.99 0 0 1 4 5a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.31-.83 2.42-2 2.83v5.29c.88-.65 2.16-1.12 4-1.12c2.67 0 3.56-1.34 3.85-2.23A3.006 3.006 0 0 1 14 7a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.34-.88 2.5-2.09 2.86C17.65 11.29 16.68 14 13 14m-6 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1M7 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1m10 2a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1z" fill="currentColor"></path></svg>
			main
			<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M7 10l5 5l5-5z" fill="currentColor"></path></svg></button>
	
	
	
	</div></div>
		<div class="flex items-center flex-wrap mb-2"><a class="hover:underline text-gray-800" href="/datasets/lewtun/github-issues/tree/main">github-issues</a>
			<span class="text-gray-300 mx-1 font-light">/</span>
				<span class="font-light dark:text-gray-300">README.md</span>

			</div></div>

	<div class="flex flex-row items-center mb-2">
		</div></header>
			<div class="border border-b-0 dark:border-gray-800 px-3 py-2 flex items-baseline rounded-t-lg bg-gradient-to-t from-gray-100-to-white"><img class="w-4 h-4 rounded-full mt-0.5 mr-2.5 self-center" alt="lewtun's picture" src="https://aeiljuispo.cloudimg.io/v7/https://s3.amazonaws.com/moonup/production/uploads/1594651707950-noauth.jpeg?w=200&amp;h=200&amp;f=face">
			<div class="mr-5 truncate flex items-center flex-none"><a class="hover:underline" href="/lewtun">lewtun
					</a>
				<div class="mt-0.5 ml-1.5 bg-yellow-50 dark:bg-yellow-800 px-1 uppercase text-xs font-semibold text-yellow-500 dark:text-yellow-400 border border-yellow-200 rounded" title="member of the Hugging Face team">HF staff
					</div>
			</div>
		<a class="mr-4 font-mono text-sm text-gray-500 truncate hover:underline" href="/datasets/lewtun/github-issues/commit/3bb24dcad2b45b45e20fc0accc93058dcbe8087d">Create README.md</a>
		<a class="text-sm border dark:border-gray-800 px-1.5 rounded bg-gray-50 dark:bg-gray-900 hover:underline" href="/datasets/lewtun/github-issues/commit/3bb24dcad2b45b45e20fc0accc93058dcbe8087d">3bb24dc</a>
		

		<time class="ml-auto hidden lg:block text-gray-500 dark:text-gray-400 truncate flex-none pl-2" datetime="2021-10-04T15:49:55" title="Mon, 04 Oct 2021 15:49:55 GMT">5 months ago</time></div>
			<div class="flex flex-wrap items-center justify-between px-3 py-1.5 border dark:border-gray-800 text-sm text-gray-800 dark:bg-gray-900"><div class="flex flex-wrap items-center"><a class="flex items-center hover:underline my-1 mr-4" href="/datasets/lewtun/github-issues/raw/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M31 16l-7 7l-1.41-1.41L28.17 16l-5.58-5.59L24 9l7 7z" fill="currentColor"></path><path d="M1 16l7-7l1.41 1.41L3.83 16l5.58 5.59L8 23l-7-7z" fill="currentColor"></path><path d="M12.419 25.484L17.639 6l1.932.518L14.35 26z" fill="currentColor"></path></svg>
								raw
							</a><a class="flex items-center hover:underline my-1 mr-4" href="/datasets/lewtun/github-issues/commits/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 4C9.383 4 4 9.383 4 16s5.383 12 12 12s12-5.383 12-12S22.617 4 16 4zm0 2c5.535 0 10 4.465 10 10s-4.465 10-10 10S6 21.535 6 16S10.465 6 16 6zm-1 2v9h7v-2h-5V8z" fill="currentColor"></path></svg>
								history
							</a><a class="flex items-center hover:underline my-1 mr-4" href="/datasets/lewtun/github-issues/blame/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12a12 12 0 0 1-12 12z" fill="currentColor"></path><path d="M11.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path><path d="M20.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path></svg>
								blame
							</a>
					<div class="text-gray-400 flex items-center"><svg class="text-gray-300 text-sm mr-1.5 -translate-y-px" width="1em" height="1em" viewBox="0 0 22 28" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.3634 10.3639C15.8486 10.8491 15.8486 11.6357 15.3634 12.1209L10.9292 16.5551C10.6058 16.8785 10.0814 16.8785 9.7579 16.5551L7.03051 13.8277C6.54532 13.3425 6.54532 12.5558 7.03051 12.0707C7.51569 11.5855 8.30234 11.5855 8.78752 12.0707L9.7579 13.041C10.0814 13.3645 10.6058 13.3645 10.9292 13.041L13.6064 10.3639C14.0916 9.8787 14.8782 9.8787 15.3634 10.3639Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M10.6666 27.12C4.93329 25.28 0 19.2267 0 12.7867V6.52001C0 5.40001 0.693334 4.41334 1.73333 4.01334L9.73333 1.01334C10.3333 0.786673 11 0.786673 11.6 1.02667L19.6 4.02667C20.1083 4.21658 20.5465 4.55701 20.8562 5.00252C21.1659 5.44803 21.3324 5.97742 21.3333 6.52001V12.7867C21.3333 19.24 16.4 25.28 10.6666 27.12Z" fill="currentColor" fill-opacity="0.22"></path><path d="M10.0845 1.94967L10.0867 1.94881C10.4587 1.8083 10.8666 1.81036 11.2286 1.95515L11.2387 1.95919L11.2489 1.963L19.2489 4.963L19.25 4.96342C19.5677 5.08211 19.8416 5.29488 20.0351 5.57333C20.2285 5.85151 20.3326 6.18203 20.3333 6.52082C20.3333 6.52113 20.3333 6.52144 20.3333 6.52176L20.3333 12.7867C20.3333 18.6535 15.8922 24.2319 10.6666 26.0652C5.44153 24.2316 1 18.6409 1 12.7867V6.52001C1 5.82357 1.42893 5.20343 2.08883 4.94803L10.0845 1.94967Z" stroke="currentColor" stroke-opacity="0.30" stroke-width="2"></path></svg>

								Safe
							</div></div>
				<div class="dark:text-gray-300">10.3 kB</div></div>

			<div class="border border-t-0 rounded-b-lg dark:bg-gray-925 dark:border-gray-800 leading-tight"><div class="py-3"><div class="SVELTE_HYDRATER contents" data-props="{&quot;lines&quot;:[&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;# Dataset Card for GitHub Issues&lt;/span&gt;&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;## Dataset Description&lt;/span&gt;&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-bullet\\&quot;&gt;-&lt;/span&gt; &lt;span class=\\&quot;hljs-strong\\&quot;&gt;**Point of Contact:**&lt;/span&gt; [&lt;span class=\\&quot;hljs-string\\&quot;&gt;Lewis Tunstall&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;lewis@huggingface.co&lt;/span&gt;)&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Dataset Summary&lt;/span&gt;&quot;,&quot;&quot;,&quot;GitHub Issues is a dataset consisting of GitHub issues and pull requests associated with the 🤗 Datasets [&lt;span class=\\&quot;hljs-string\\&quot;&gt;repository&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://github.com/huggingface/datasets&lt;/span&gt;). It is intended for educational purposes and can be used for semantic search or multilabel text classification. The contents of each GitHub issue are in English and concern the domain of datasets for NLP, computer vision, and beyond.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Supported Tasks and Leaderboards&lt;/span&gt;&quot;,&quot;&quot;,&quot;For each of the tasks tagged for this dataset, give a brief description of the tag, metrics, and suggested models (with a link to their HuggingFace implementation if available). Give a similar description of tasks that were not covered by the structured tag set (repace the &lt;span class=\\&quot;hljs-code\\&quot;&gt;`task-category-tag`&lt;/span&gt; with an appropriate &lt;span class=\\&quot;hljs-code\\&quot;&gt;`other:other-task-name`&lt;/span&gt;).&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-bullet\\&quot;&gt;-&lt;/span&gt; &lt;span class=\\&quot;hljs-code\\&quot;&gt;`task-category-tag`&lt;/span&gt;: The dataset can be used to train a model for [&lt;span class=\\&quot;hljs-string\\&quot;&gt;TASK NAME&lt;/span&gt;], which consists in [&lt;span class=\\&quot;hljs-string\\&quot;&gt;TASK DESCRIPTION&lt;/span&gt;]. Success on this task is typically measured by achieving a &lt;span class=\\&quot;hljs-emphasis\\&quot;&gt;*high/low*&lt;/span&gt; [&lt;span class=\\&quot;hljs-string\\&quot;&gt;metric name&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://huggingface.co/metrics/metric_name&lt;/span&gt;). The ([&lt;span class=\\&quot;hljs-string\\&quot;&gt;model name&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://huggingface.co/model_name&lt;/span&gt;) or [&lt;span class=\\&quot;hljs-string\\&quot;&gt;model class&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://huggingface.co/transformers/model_doc/model_class.html&lt;/span&gt;)) model currently achieves the following score. &lt;span class=\\&quot;hljs-emphasis\\&quot;&gt;*[&lt;span class=\\&quot;hljs-string\\&quot;&gt;IF A LEADERBOARD IS AVAILABLE&lt;/span&gt;]:*&lt;/span&gt; This task has an active leaderboard which can be found at [&lt;span class=\\&quot;hljs-string\\&quot;&gt;leaderboard url&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;&lt;/span&gt;) and ranks models based on [&lt;span class=\\&quot;hljs-string\\&quot;&gt;metric name&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://huggingface.co/metrics/metric_name&lt;/span&gt;) while also reporting [&lt;span class=\\&quot;hljs-string\\&quot;&gt;other metric name&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://huggingface.co/metrics/other_metric_name&lt;/span&gt;).&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Languages&lt;/span&gt;&quot;,&quot;&quot;,&quot;Provide a brief overview of the languages represented in the dataset. Describe relevant details about specifics of the language such as whether it is social media text, African American English,...&quot;,&quot;&quot;,&quot;When relevant, please provide [&lt;span class=\\&quot;hljs-string\\&quot;&gt;BCP-47 codes&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://tools.ietf.org/html/bcp47&lt;/span&gt;), which consist of a [&lt;span class=\\&quot;hljs-string\\&quot;&gt;primary language subtag&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://tools.ietf.org/html/bcp47#section-2.2.1&lt;/span&gt;), with a [&lt;span class=\\&quot;hljs-string\\&quot;&gt;script subtag&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://tools.ietf.org/html/bcp47#section-2.2.3&lt;/span&gt;) and/or [&lt;span class=\\&quot;hljs-string\\&quot;&gt;region subtag&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://tools.ietf.org/html/bcp47#section-2.2.4&lt;/span&gt;) if available.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;## Dataset Structure&lt;/span&gt;&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Data Instances&lt;/span&gt;&quot;,&quot;&quot;,&quot;Provide an JSON-formatted example and brief description of a typical instance in the dataset. If available, provide a link to further examples.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;```&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;{&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;  &amp;#x27;example_field&amp;#x27;: ...,&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;  ...&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;}&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;```&lt;/span&gt;&quot;,&quot;&quot;,&quot;Provide any additional information that is not covered in the other sections about the data here. In particular describe any relationships between data points and if these relationships are made explicit.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Data Fields&lt;/span&gt;&quot;,&quot;&quot;,&quot;List and describe the fields present in the dataset. Mention their data type, and whether they are used as input or output in any of the tasks the dataset currently supports. If the data has span indices, describe their attributes, such as whether they are at the character level or word level, whether they are contiguous or not, etc. If the datasets contains example IDs, state whether they have an inherent meaning, such as a mapping to other datasets or pointing to relationships between data points.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-bullet\\&quot;&gt;-&lt;/span&gt; &lt;span class=\\&quot;hljs-code\\&quot;&gt;`example_field`&lt;/span&gt;: description of &lt;span class=\\&quot;hljs-code\\&quot;&gt;`example_field`&lt;/span&gt;&quot;,&quot;&quot;,&quot;Note that the descriptions can be initialized with the &lt;span class=\\&quot;hljs-strong\\&quot;&gt;**Show Markdown Data Fields**&lt;/span&gt; output of the [&lt;span class=\\&quot;hljs-string\\&quot;&gt;tagging app&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://github.com/huggingface/datasets-tagging&lt;/span&gt;), you will then only need to refine the generated descriptions.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Data Splits&lt;/span&gt;&quot;,&quot;&quot;,&quot;Describe and name the splits in the dataset if there are more than one.&quot;,&quot;&quot;,&quot;Describe any criteria for splitting the data, if used. If their are differences between the splits (e.g. if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here.&quot;,&quot;&quot;,&quot;Provide the sizes of each split. As appropriate, provide any descriptive statistics for the features, such as average length.  For example:&quot;,&quot;&quot;,&quot;|                            | Tain   | Valid | Test |&quot;,&quot;| -----                      | ------ | ----- | ---- |&quot;,&quot;| Input Sentences            |        |       |      |&quot;,&quot;| Average Sentence Length    |        |       |      |&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;## Dataset Creation&lt;/span&gt;&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Curation Rationale&lt;/span&gt;&quot;,&quot;&quot;,&quot;What need motivated the creation of this dataset? What are some of the reasons underlying the major choices involved in putting it together?&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Source Data&lt;/span&gt;&quot;,&quot;&quot;,&quot;This section describes the source data (e.g. news text and headlines, social media posts, translated sentences,...)&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;#### Initial Data Collection and Normalization&lt;/span&gt;&quot;,&quot;&quot;,&quot;Describe the data collection process. Describe any criteria for data selection or filtering. List any key words or search terms used. If possible, include runtime information for the collection process.&quot;,&quot;&quot;,&quot;If data was collected from other pre-existing datasets, link to source here and to their [&lt;span class=\\&quot;hljs-string\\&quot;&gt;Hugging Face version&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://huggingface.co/datasets/dataset_name&lt;/span&gt;).&quot;,&quot;&quot;,&quot;If the data was modified or normalized after being collected (e.g. if the data is word-tokenized), describe the process and the tools used.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;#### Who are the source language producers?&lt;/span&gt;&quot;,&quot;&quot;,&quot;State whether the data was produced by humans or machine generated. Describe the people or systems who originally created the data.&quot;,&quot;&quot;,&quot;If available, include self-reported demographic or identity information for the source data creators, but avoid inferring this information. Instead state that this information is unknown. See [&lt;span class=\\&quot;hljs-string\\&quot;&gt;Larson 2017&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://www.aclweb.org/anthology/W17-1601.pdf&lt;/span&gt;) for using identity categories as a variables, particularly gender.&quot;,&quot;&quot;,&quot;Describe the conditions under which the data was created (for example, if the producers were crowdworkers, state what platform was used, or if the data was found, what website the data was found on). If compensation was provided, include that information here.&quot;,&quot;&quot;,&quot;Describe other people represented or mentioned in the data. Where possible, link to references for the information.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Annotations&lt;/span&gt;&quot;,&quot;&quot;,&quot;If the dataset contains annotations which are not part of the initial data collection, describe them in the following paragraphs.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;#### Annotation process&lt;/span&gt;&quot;,&quot;&quot;,&quot;If applicable, describe the annotation process and any tools used, or state otherwise. Describe the amount of data annotated, if not all. Describe or reference annotation guidelines provided to the annotators. If available, provide interannotator statistics. Describe any annotation validation processes.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;#### Who are the annotators?&lt;/span&gt;&quot;,&quot;&quot;,&quot;If annotations were collected for the source data (such as class labels or syntactic parses), state whether the annotations were produced by humans or machine generated.&quot;,&quot;&quot;,&quot;Describe the people or systems who originally created the annotations and their selection criteria if applicable.&quot;,&quot;&quot;,&quot;If available, include self-reported demographic or identity information for the annotators, but avoid inferring this information. Instead state that this information is unknown. See [&lt;span class=\\&quot;hljs-string\\&quot;&gt;Larson 2017&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://www.aclweb.org/anthology/W17-1601.pdf&lt;/span&gt;) for using identity categories as a variables, particularly gender.&quot;,&quot;&quot;,&quot;Describe the conditions under which the data was annotated (for example, if the annotators were crowdworkers, state what platform was used, or if the data was found, what website the data was found on). If compensation was provided, include that information here.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Personal and Sensitive Information&lt;/span&gt;&quot;,&quot;&quot;,&quot;State whether the dataset uses identity categories and, if so, how the information is used. Describe where this information comes from (i.e. self-reporting, collecting from profiles, inferring, etc.). See [&lt;span class=\\&quot;hljs-string\\&quot;&gt;Larson 2017&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://www.aclweb.org/anthology/W17-1601.pdf&lt;/span&gt;) for using identity categories as a variables, particularly gender. State whether the data is linked to individuals and whether those individuals can be identified in the dataset, either directly or indirectly (i.e., in combination with other data).&quot;,&quot;&quot;,&quot;State whether the dataset contains other data that might be considered sensitive (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history).  &quot;,&quot;&quot;,&quot;If efforts were made to anonymize the data, describe the anonymization process.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;## Considerations for Using the Data&lt;/span&gt;&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Social Impact of Dataset&lt;/span&gt;&quot;,&quot;&quot;,&quot;Please discuss some of the ways you believe the use of this dataset will impact society.&quot;,&quot;&quot;,&quot;The statement should include both positive outlooks, such as outlining how technologies developed through its use may improve people&amp;#x27;s lives, and discuss the accompanying risks. These risks may range from making important decisions more opaque to people who are affected by the technology, to reinforcing existing harmful biases (whose specifics should be discussed in the next section), among other considerations.&quot;,&quot;&quot;,&quot;Also describe in this section if the proposed dataset contains a low-resource or under-represented language. If this is the case or if this task has any impact on underserved communities, please elaborate here.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Discussion of Biases&lt;/span&gt;&quot;,&quot;&quot;,&quot;Provide descriptions of specific biases that are likely to be reflected in the data, and state whether any steps were taken to reduce their impact.&quot;,&quot;&quot;,&quot;For Wikipedia text, see for example [&lt;span class=\\&quot;hljs-string\\&quot;&gt;Dinan et al 2020 on biases in Wikipedia (esp. Table 1)&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://arxiv.org/abs/2005.00614&lt;/span&gt;), or [&lt;span class=\\&quot;hljs-string\\&quot;&gt;Blodgett et al 2020&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://www.aclweb.org/anthology/2020.acl-main.485/&lt;/span&gt;) for a more general discussion of the topic.&quot;,&quot;&quot;,&quot;If analyses have been run quantifying these biases, please add brief summaries and links to the studies here.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Other Known Limitations&lt;/span&gt;&quot;,&quot;&quot;,&quot;If studies of the datasets have outlined other limitations of the dataset, such as annotation artifacts, please outline and cite them here.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;## Additional Information&lt;/span&gt;&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Dataset Curators&lt;/span&gt;&quot;,&quot;&quot;,&quot;List the people involved in collecting the dataset and their affiliation(s). If funding information is known, include it here.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Licensing Information&lt;/span&gt;&quot;,&quot;&quot;,&quot;Provide the license and link to the license webpage if available.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Citation Information&lt;/span&gt;&quot;,&quot;&quot;,&quot;Provide the [&lt;span class=\\&quot;hljs-string\\&quot;&gt;BibTex&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;http://www.bibtex.org/&lt;/span&gt;)-formatted reference for the dataset. For example:&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;```&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;@article{article_id,&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;  author    = {Author List},&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;  title     = {Dataset Paper Title},&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;  journal   = {Publication Venue},&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;  year      = {2525}&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;}&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-code\\&quot;&gt;```&lt;/span&gt;&quot;,&quot;&quot;,&quot;If the dataset has a [&lt;span class=\\&quot;hljs-string\\&quot;&gt;DOI&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://www.doi.org/&lt;/span&gt;), please provide it here.&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-section\\&quot;&gt;### Contributions&lt;/span&gt;&quot;,&quot;&quot;,&quot;Thanks to [&lt;span class=\\&quot;hljs-string\\&quot;&gt;@lewtun&lt;/span&gt;](&lt;span class=\\&quot;hljs-link\\&quot;&gt;https://github.com/lewtun&lt;/span&gt;) for adding this dataset.&quot;]}" data-target="BlobContent"><div class="relative text-sm"><div class="overflow-x-auto"><table class="border-collapse font-mono"><tbody><tr class="" id="L1"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">1</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section"># Dataset Card for GitHub Issues</span></td>
					</tr><tr class="" id="L2"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">2</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L3"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">3</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">## Dataset Description</span></td>
					</tr><tr class="" id="L4"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">4</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L5"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">5</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-bullet">-</span> <span class="hljs-strong">**Point of Contact:**</span> [<span class="hljs-string">Lewis Tunstall</span>](<span class="hljs-link">lewis@huggingface.co</span>)</td>
					</tr><tr class="" id="L6"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">6</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L7"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">7</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Dataset Summary</span></td>
					</tr><tr class="" id="L8"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">8</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L9"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">9</td>
						<td class="px-3 overflow-visible whitespace-pre">GitHub Issues is a dataset consisting of GitHub issues and pull requests associated with the 🤗 Datasets [<span class="hljs-string">repository</span>](<span class="hljs-link">https://github.com/huggingface/datasets</span>). It is intended for educational purposes and can be used for semantic search or multilabel text classification. The contents of each GitHub issue are in English and concern the domain of datasets for NLP, computer vision, and beyond.</td>
					</tr><tr class="" id="L10"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">10</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L11"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">11</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Supported Tasks and Leaderboards</span></td>
					</tr><tr class="" id="L12"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">12</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L13"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">13</td>
						<td class="px-3 overflow-visible whitespace-pre">For each of the tasks tagged for this dataset, give a brief description of the tag, metrics, and suggested models (with a link to their HuggingFace implementation if available). Give a similar description of tasks that were not covered by the structured tag set (repace the <span class="hljs-code">`task-category-tag`</span> with an appropriate <span class="hljs-code">`other:other-task-name`</span>).</td>
					</tr><tr class="" id="L14"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">14</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L15"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">15</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-bullet">-</span> <span class="hljs-code">`task-category-tag`</span>: The dataset can be used to train a model for [<span class="hljs-string">TASK NAME</span>], which consists in [<span class="hljs-string">TASK DESCRIPTION</span>]. Success on this task is typically measured by achieving a <span class="hljs-emphasis">*high/low*</span> [<span class="hljs-string">metric name</span>](<span class="hljs-link">https://huggingface.co/metrics/metric_name</span>). The ([<span class="hljs-string">model name</span>](<span class="hljs-link">https://huggingface.co/model_name</span>) or [<span class="hljs-string">model class</span>](<span class="hljs-link">https://huggingface.co/transformers/model_doc/model_class.html</span>)) model currently achieves the following score. <span class="hljs-emphasis">*[<span class="hljs-string">IF A LEADERBOARD IS AVAILABLE</span>]:*</span> This task has an active leaderboard which can be found at [<span class="hljs-string">leaderboard url</span>](<span class="hljs-link"></span>) and ranks models based on [<span class="hljs-string">metric name</span>](<span class="hljs-link">https://huggingface.co/metrics/metric_name</span>) while also reporting [<span class="hljs-string">other metric name</span>](<span class="hljs-link">https://huggingface.co/metrics/other_metric_name</span>).</td>
					</tr><tr class="" id="L16"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">16</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L17"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">17</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Languages</span></td>
					</tr><tr class="" id="L18"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">18</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L19"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">19</td>
						<td class="px-3 overflow-visible whitespace-pre">Provide a brief overview of the languages represented in the dataset. Describe relevant details about specifics of the language such as whether it is social media text, African American English,...</td>
					</tr><tr class="" id="L20"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">20</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L21"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">21</td>
						<td class="px-3 overflow-visible whitespace-pre">When relevant, please provide [<span class="hljs-string">BCP-47 codes</span>](<span class="hljs-link">https://tools.ietf.org/html/bcp47</span>), which consist of a [<span class="hljs-string">primary language subtag</span>](<span class="hljs-link">https://tools.ietf.org/html/bcp47#section-2.2.1</span>), with a [<span class="hljs-string">script subtag</span>](<span class="hljs-link">https://tools.ietf.org/html/bcp47#section-2.2.3</span>) and/or [<span class="hljs-string">region subtag</span>](<span class="hljs-link">https://tools.ietf.org/html/bcp47#section-2.2.4</span>) if available.</td>
					</tr><tr class="" id="L22"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">22</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L23"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">23</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">## Dataset Structure</span></td>
					</tr><tr class="" id="L24"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">24</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L25"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">25</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Data Instances</span></td>
					</tr><tr class="" id="L26"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">26</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L27"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">27</td>
						<td class="px-3 overflow-visible whitespace-pre">Provide an JSON-formatted example and brief description of a typical instance in the dataset. If available, provide a link to further examples.</td>
					</tr><tr class="" id="L28"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">28</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L29"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">29</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">```</span></td>
					</tr><tr class="" id="L30"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">30</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">{</span></td>
					</tr><tr class="" id="L31"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">31</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">  &#x27;example_field&#x27;: ...,</span></td>
					</tr><tr class="" id="L32"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">32</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">  ...</span></td>
					</tr><tr class="" id="L33"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">33</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">}</span></td>
					</tr><tr class="" id="L34"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">34</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">```</span></td>
					</tr><tr class="" id="L35"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">35</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L36"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">36</td>
						<td class="px-3 overflow-visible whitespace-pre">Provide any additional information that is not covered in the other sections about the data here. In particular describe any relationships between data points and if these relationships are made explicit.</td>
					</tr><tr class="" id="L37"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">37</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L38"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">38</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Data Fields</span></td>
					</tr><tr class="" id="L39"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">39</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L40"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">40</td>
						<td class="px-3 overflow-visible whitespace-pre">List and describe the fields present in the dataset. Mention their data type, and whether they are used as input or output in any of the tasks the dataset currently supports. If the data has span indices, describe their attributes, such as whether they are at the character level or word level, whether they are contiguous or not, etc. If the datasets contains example IDs, state whether they have an inherent meaning, such as a mapping to other datasets or pointing to relationships between data points.</td>
					</tr><tr class="" id="L41"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">41</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L42"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">42</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-bullet">-</span> <span class="hljs-code">`example_field`</span>: description of <span class="hljs-code">`example_field`</span></td>
					</tr><tr class="" id="L43"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">43</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L44"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">44</td>
						<td class="px-3 overflow-visible whitespace-pre">Note that the descriptions can be initialized with the <span class="hljs-strong">**Show Markdown Data Fields**</span> output of the [<span class="hljs-string">tagging app</span>](<span class="hljs-link">https://github.com/huggingface/datasets-tagging</span>), you will then only need to refine the generated descriptions.</td>
					</tr><tr class="" id="L45"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">45</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L46"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">46</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Data Splits</span></td>
					</tr><tr class="" id="L47"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">47</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L48"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">48</td>
						<td class="px-3 overflow-visible whitespace-pre">Describe and name the splits in the dataset if there are more than one.</td>
					</tr><tr class="" id="L49"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">49</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L50"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">50</td>
						<td class="px-3 overflow-visible whitespace-pre">Describe any criteria for splitting the data, if used. If their are differences between the splits (e.g. if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here.</td>
					</tr><tr class="" id="L51"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">51</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L52"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">52</td>
						<td class="px-3 overflow-visible whitespace-pre">Provide the sizes of each split. As appropriate, provide any descriptive statistics for the features, such as average length.  For example:</td>
					</tr><tr class="" id="L53"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">53</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L54"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">54</td>
						<td class="px-3 overflow-visible whitespace-pre">|                            | Tain   | Valid | Test |</td>
					</tr><tr class="" id="L55"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">55</td>
						<td class="px-3 overflow-visible whitespace-pre">| -----                      | ------ | ----- | ---- |</td>
					</tr><tr class="" id="L56"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">56</td>
						<td class="px-3 overflow-visible whitespace-pre">| Input Sentences            |        |       |      |</td>
					</tr><tr class="" id="L57"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">57</td>
						<td class="px-3 overflow-visible whitespace-pre">| Average Sentence Length    |        |       |      |</td>
					</tr><tr class="" id="L58"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">58</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L59"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">59</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">## Dataset Creation</span></td>
					</tr><tr class="" id="L60"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">60</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L61"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">61</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Curation Rationale</span></td>
					</tr><tr class="" id="L62"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">62</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L63"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">63</td>
						<td class="px-3 overflow-visible whitespace-pre">What need motivated the creation of this dataset? What are some of the reasons underlying the major choices involved in putting it together?</td>
					</tr><tr class="" id="L64"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">64</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L65"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">65</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Source Data</span></td>
					</tr><tr class="" id="L66"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">66</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L67"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">67</td>
						<td class="px-3 overflow-visible whitespace-pre">This section describes the source data (e.g. news text and headlines, social media posts, translated sentences,...)</td>
					</tr><tr class="" id="L68"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">68</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L69"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">69</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">#### Initial Data Collection and Normalization</span></td>
					</tr><tr class="" id="L70"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">70</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L71"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">71</td>
						<td class="px-3 overflow-visible whitespace-pre">Describe the data collection process. Describe any criteria for data selection or filtering. List any key words or search terms used. If possible, include runtime information for the collection process.</td>
					</tr><tr class="" id="L72"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">72</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L73"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">73</td>
						<td class="px-3 overflow-visible whitespace-pre">If data was collected from other pre-existing datasets, link to source here and to their [<span class="hljs-string">Hugging Face version</span>](<span class="hljs-link">https://huggingface.co/datasets/dataset_name</span>).</td>
					</tr><tr class="" id="L74"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">74</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L75"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">75</td>
						<td class="px-3 overflow-visible whitespace-pre">If the data was modified or normalized after being collected (e.g. if the data is word-tokenized), describe the process and the tools used.</td>
					</tr><tr class="" id="L76"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">76</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L77"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">77</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">#### Who are the source language producers?</span></td>
					</tr><tr class="" id="L78"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">78</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L79"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">79</td>
						<td class="px-3 overflow-visible whitespace-pre">State whether the data was produced by humans or machine generated. Describe the people or systems who originally created the data.</td>
					</tr><tr class="" id="L80"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">80</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L81"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">81</td>
						<td class="px-3 overflow-visible whitespace-pre">If available, include self-reported demographic or identity information for the source data creators, but avoid inferring this information. Instead state that this information is unknown. See [<span class="hljs-string">Larson 2017</span>](<span class="hljs-link">https://www.aclweb.org/anthology/W17-1601.pdf</span>) for using identity categories as a variables, particularly gender.</td>
					</tr><tr class="" id="L82"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">82</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L83"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">83</td>
						<td class="px-3 overflow-visible whitespace-pre">Describe the conditions under which the data was created (for example, if the producers were crowdworkers, state what platform was used, or if the data was found, what website the data was found on). If compensation was provided, include that information here.</td>
					</tr><tr class="" id="L84"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">84</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L85"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">85</td>
						<td class="px-3 overflow-visible whitespace-pre">Describe other people represented or mentioned in the data. Where possible, link to references for the information.</td>
					</tr><tr class="" id="L86"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">86</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L87"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">87</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Annotations</span></td>
					</tr><tr class="" id="L88"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">88</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L89"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">89</td>
						<td class="px-3 overflow-visible whitespace-pre">If the dataset contains annotations which are not part of the initial data collection, describe them in the following paragraphs.</td>
					</tr><tr class="" id="L90"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">90</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L91"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">91</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">#### Annotation process</span></td>
					</tr><tr class="" id="L92"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">92</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L93"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">93</td>
						<td class="px-3 overflow-visible whitespace-pre">If applicable, describe the annotation process and any tools used, or state otherwise. Describe the amount of data annotated, if not all. Describe or reference annotation guidelines provided to the annotators. If available, provide interannotator statistics. Describe any annotation validation processes.</td>
					</tr><tr class="" id="L94"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">94</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L95"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">95</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">#### Who are the annotators?</span></td>
					</tr><tr class="" id="L96"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">96</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L97"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">97</td>
						<td class="px-3 overflow-visible whitespace-pre">If annotations were collected for the source data (such as class labels or syntactic parses), state whether the annotations were produced by humans or machine generated.</td>
					</tr><tr class="" id="L98"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">98</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L99"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">99</td>
						<td class="px-3 overflow-visible whitespace-pre">Describe the people or systems who originally created the annotations and their selection criteria if applicable.</td>
					</tr><tr class="" id="L100"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">100</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L101"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">101</td>
						<td class="px-3 overflow-visible whitespace-pre">If available, include self-reported demographic or identity information for the annotators, but avoid inferring this information. Instead state that this information is unknown. See [<span class="hljs-string">Larson 2017</span>](<span class="hljs-link">https://www.aclweb.org/anthology/W17-1601.pdf</span>) for using identity categories as a variables, particularly gender.</td>
					</tr><tr class="" id="L102"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">102</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L103"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">103</td>
						<td class="px-3 overflow-visible whitespace-pre">Describe the conditions under which the data was annotated (for example, if the annotators were crowdworkers, state what platform was used, or if the data was found, what website the data was found on). If compensation was provided, include that information here.</td>
					</tr><tr class="" id="L104"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">104</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L105"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">105</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Personal and Sensitive Information</span></td>
					</tr><tr class="" id="L106"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">106</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L107"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">107</td>
						<td class="px-3 overflow-visible whitespace-pre">State whether the dataset uses identity categories and, if so, how the information is used. Describe where this information comes from (i.e. self-reporting, collecting from profiles, inferring, etc.). See [<span class="hljs-string">Larson 2017</span>](<span class="hljs-link">https://www.aclweb.org/anthology/W17-1601.pdf</span>) for using identity categories as a variables, particularly gender. State whether the data is linked to individuals and whether those individuals can be identified in the dataset, either directly or indirectly (i.e., in combination with other data).</td>
					</tr><tr class="" id="L108"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">108</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L109"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">109</td>
						<td class="px-3 overflow-visible whitespace-pre">State whether the dataset contains other data that might be considered sensitive (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history).  </td>
					</tr><tr class="" id="L110"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">110</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L111"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">111</td>
						<td class="px-3 overflow-visible whitespace-pre">If efforts were made to anonymize the data, describe the anonymization process.</td>
					</tr><tr class="" id="L112"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">112</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L113"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">113</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">## Considerations for Using the Data</span></td>
					</tr><tr class="" id="L114"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">114</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L115"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">115</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Social Impact of Dataset</span></td>
					</tr><tr class="" id="L116"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">116</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L117"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">117</td>
						<td class="px-3 overflow-visible whitespace-pre">Please discuss some of the ways you believe the use of this dataset will impact society.</td>
					</tr><tr class="" id="L118"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">118</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L119"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">119</td>
						<td class="px-3 overflow-visible whitespace-pre">The statement should include both positive outlooks, such as outlining how technologies developed through its use may improve people&#x27;s lives, and discuss the accompanying risks. These risks may range from making important decisions more opaque to people who are affected by the technology, to reinforcing existing harmful biases (whose specifics should be discussed in the next section), among other considerations.</td>
					</tr><tr class="" id="L120"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">120</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L121"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">121</td>
						<td class="px-3 overflow-visible whitespace-pre">Also describe in this section if the proposed dataset contains a low-resource or under-represented language. If this is the case or if this task has any impact on underserved communities, please elaborate here.</td>
					</tr><tr class="" id="L122"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">122</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L123"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">123</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Discussion of Biases</span></td>
					</tr><tr class="" id="L124"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">124</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L125"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">125</td>
						<td class="px-3 overflow-visible whitespace-pre">Provide descriptions of specific biases that are likely to be reflected in the data, and state whether any steps were taken to reduce their impact.</td>
					</tr><tr class="" id="L126"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">126</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L127"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">127</td>
						<td class="px-3 overflow-visible whitespace-pre">For Wikipedia text, see for example [<span class="hljs-string">Dinan et al 2020 on biases in Wikipedia (esp. Table 1)</span>](<span class="hljs-link">https://arxiv.org/abs/2005.00614</span>), or [<span class="hljs-string">Blodgett et al 2020</span>](<span class="hljs-link">https://www.aclweb.org/anthology/2020.acl-main.485/</span>) for a more general discussion of the topic.</td>
					</tr><tr class="" id="L128"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">128</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L129"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">129</td>
						<td class="px-3 overflow-visible whitespace-pre">If analyses have been run quantifying these biases, please add brief summaries and links to the studies here.</td>
					</tr><tr class="" id="L130"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">130</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L131"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">131</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Other Known Limitations</span></td>
					</tr><tr class="" id="L132"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">132</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L133"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">133</td>
						<td class="px-3 overflow-visible whitespace-pre">If studies of the datasets have outlined other limitations of the dataset, such as annotation artifacts, please outline and cite them here.</td>
					</tr><tr class="" id="L134"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">134</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L135"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">135</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">## Additional Information</span></td>
					</tr><tr class="" id="L136"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">136</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L137"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">137</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Dataset Curators</span></td>
					</tr><tr class="" id="L138"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">138</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L139"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">139</td>
						<td class="px-3 overflow-visible whitespace-pre">List the people involved in collecting the dataset and their affiliation(s). If funding information is known, include it here.</td>
					</tr><tr class="" id="L140"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">140</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L141"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">141</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Licensing Information</span></td>
					</tr><tr class="" id="L142"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">142</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L143"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">143</td>
						<td class="px-3 overflow-visible whitespace-pre">Provide the license and link to the license webpage if available.</td>
					</tr><tr class="" id="L144"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">144</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L145"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">145</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Citation Information</span></td>
					</tr><tr class="" id="L146"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">146</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L147"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">147</td>
						<td class="px-3 overflow-visible whitespace-pre">Provide the [<span class="hljs-string">BibTex</span>](<span class="hljs-link">http://www.bibtex.org/</span>)-formatted reference for the dataset. For example:</td>
					</tr><tr class="" id="L148"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">148</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">```</span></td>
					</tr><tr class="" id="L149"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">149</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">@article{article_id,</span></td>
					</tr><tr class="" id="L150"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">150</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">  author    = {Author List},</span></td>
					</tr><tr class="" id="L151"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">151</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">  title     = {Dataset Paper Title},</span></td>
					</tr><tr class="" id="L152"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">152</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">  journal   = {Publication Venue},</span></td>
					</tr><tr class="" id="L153"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">153</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">  year      = {2525}</span></td>
					</tr><tr class="" id="L154"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">154</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">}</span></td>
					</tr><tr class="" id="L155"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">155</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-code">```</span></td>
					</tr><tr class="" id="L156"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">156</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L157"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">157</td>
						<td class="px-3 overflow-visible whitespace-pre">If the dataset has a [<span class="hljs-string">DOI</span>](<span class="hljs-link">https://www.doi.org/</span>), please provide it here.</td>
					</tr><tr class="" id="L158"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">158</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L159"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">159</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-section">### Contributions</span></td>
					</tr><tr class="" id="L160"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">160</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L161"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">161</td>
						<td class="px-3 overflow-visible whitespace-pre">Thanks to [<span class="hljs-string">@lewtun</span>](<span class="hljs-link">https://github.com/lewtun</span>) for adding this dataset.</td>
					</tr></tbody></table></div>
	</div></div></div></div></section></div></main>
	</div>

		<script>
			import("/front/build/module/index.6509d170.js");
			window.supportsDynamicImport = true;
		</script>
		<script>
			if (!window.supportsDynamicImport) {
				const systemJsLoaderTag = document.createElement("script");
				systemJsLoaderTag.src =
					"https://unpkg.com/systemjs@2.0.0/dist/s.min.js";
				systemJsLoaderTag.addEventListener("load", function () {
					System.import("./front/build/nomodule/index.6509d170.js");
				});
				document.head.appendChild(systemJsLoaderTag);
			}
		</script>

		<script type="text/javascript">
			/// LinkedIn (part 1)
			_linkedin_partner_id = "3734489";
			window._linkedin_data_partner_ids =
				window._linkedin_data_partner_ids || [];
			window._linkedin_data_partner_ids.push(_linkedin_partner_id);
		</script>

		<script>
			if (
				!(
					["localhost", "huggingface.test"].includes(
						window.location.hostname
					) || window.location.hostname.includes("ngrok.io")
				)
			) {
				(function (i, s, o, g, r, a, m) {
					i["GoogleAnalyticsObject"] = r;
					(i[r] =
						i[r] ||
						function () {
							(i[r].q = i[r].q || []).push(arguments);
						}),
						(i[r].l = 1 * new Date());
					(a = s.createElement(o)), (m = s.getElementsByTagName(o)[0]);
					a.async = 1;
					a.src = g;
					m.parentNode.insertBefore(a, m);
				})(
					window,
					document,
					"script",
					"https://www.google-analytics.com/analytics.js",
					"ganalytics"
				);
				ganalytics("create", "UA-83738774-2", "auto");
				ganalytics("send", "pageview");

				/// LinkedIn (part 2)
				(function (l) {
					if (!l) {
						window.lintrk = function (a, b) {
							window.lintrk.q.push([a, b]);
						};
						window.lintrk.q = [];
					}
					var s = document.getElementsByTagName("script")[0];
					var b = document.createElement("script");
					b.type = "text/javascript";
					b.async = true;
					b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
					s.parentNode.insertBefore(b, s);
				})(window.lintrk);

				/// Twitter
				!(function (e, t, n, s, u, a) {
					e.twq ||
						((s = e.twq =
							function () {
								s.exe ? s.exe.apply(s, arguments) : s.queue.push(arguments);
							}),
						(s.version = "1.1"),
						(s.queue = []),
						(u = t.createElement(n)),
						(u.async = !0),
						(u.src = "//static.ads-twitter.com/uwt.js"),
						(a = t.getElementsByTagName(n)[0]),
						a.parentNode.insertBefore(u, a));
				})(window, document, "script");
				twq("init", "o6bfm");
				twq("track", "PageView");
			}
		</script>

		<noscript>
			<!-- LinkedIn (part 3) -->
			<img
				height="1"
				width="1"
				style="display: none"
				alt=""
				src="https://px.ads.linkedin.com/collect/?pid=3734489&fmt=gif"
			/>
		</noscript>
	</body>
</html>
