import axios from 'axios'

export const search = async text => {
    try {
        const data = {
            "data": text
        }
        
        let res = await axios.post(process.env.VUE_APP_API_ENDPOINT+'/search', data)

        if (res.status == 200 && res.data) {
            return res.data.search_results
        }
    } catch(e) {
        console.error(e)
    }
}

export const suggest = async text => {
    try {
        const data = {
            "data": text
        }

        let res = await axios.post(process.env.VUE_APP_API_ENDPOINT+'/suggest', data)

        if (res.status == 200 && res.data) {
            let newSuggestions = res.data.suggestions

            return newSuggestions.length > 0 ? newSuggestions : null
        }
    } catch (e) {
        console.error(e);
    }
}

export const searchPage = async (text, page) => {
    try {
        const data = {
            "data": text,
            page
        }
        
        let res = await axios.post(process.env.VUE_APP_API_ENDPOINT+'/search_page', data)

        if (res.status == 200 && res.data) {
            return res.data.search_results
        }
    } catch(e) {
        console.error(e)
    }
}