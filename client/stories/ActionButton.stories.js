import { action } from '@storybook/addon-actions';
import { linkTo } from '@storybook/addon-links';

import ActionButton from '../src/components/atoms/ActionButton';

export default {
  title: 'Action Button',
  component: ActionButton,
};

export const Text = () => ({
  components: { 
    ActionButton 
  },
  template: '<action-button @click="action">Hello Button</action-button>',
  methods: { 
    action: action('clicked') 
  },
});

export const Jsx = () => ({
  components: { ActionButton },
  render(h) {
    return <action-button onClick={this.action}>With JSX</action-button>;
  },
  methods: { action: linkTo('clicked') },
});

export const Emoji = () => ({
  components: { ActionButton },
  template: '<action-button @click="action">😀 😎 👍 💯</action-button>',
  methods: { action: action('clicked') },
});
