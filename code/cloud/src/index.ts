import { Request, Response } from 'express';
import paths from './common/paths';

import getDelivery from './deliveries/getDelivery';
import setDelivered from './deliveries/setDelivered';
import createDelivery from './deliveries/createDelivery';

import setOptions from './options/setOptions';
import getOptions from './options/getOptions';

export const delivery_handler = (req: Request, res: Response) => {
  switch (req.path) {
    case paths.GET_DELIVERY:
      getDelivery(req, res);
      break;
    case paths.SET_DELIVERED:
      setDelivered(req, res);
      break;
    case paths.CREATE_DELIVERY:
      createDelivery(req, res);
      break;
    default:
      res.status(500).send(`Invalid Path ${req.path}`);
  }
};

export const option_handler = (req: Request, res: Response) => {
  switch (req.path) {
    case paths.GET_OPTIONS:
      setOptions(req, res);
      break;
    case paths.SET_OPTIONS:
      getOptions(req, res);
      break;
    default:
      res.status(500).send(`Invalid Path ${req.path}`);
  }
};
