import { Request, Response } from 'express'
import paths from '../common/paths'

import getDelivery from './getDelivery';
import setDelivered from './setDelivered';
import createDelivery from './createDelivery';

export const delivery_handler = (req: Request, res: Response) => {
  switch(req.path) {
    case paths.GET_DELIVERY:
      getDelivery(req,res)
    break;
    case paths.SET_DELIVERED:
      setDelivered(req,res);
    break;
    case paths.CREATE_DELIVERY:
      createDelivery(req,res)
    break;
    default: res.status(500).send(`Invalid Path ${req.path}`)
  }
};