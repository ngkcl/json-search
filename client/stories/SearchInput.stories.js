import { action } from '@storybook/addon-actions';
import { linkTo } from '@storybook/addon-links';

import SearchInput from '../src/components/molecules/SearchInput';

export default {
  title: 'Search Input',
  component: SearchInput,
};

export const Empty = () => ({
  components: { 
    SearchInput 
  },
  template: '<search-input></search-input>'
});